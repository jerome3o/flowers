from anthropic import Anthropic
from pathlib import Path
from anthropic.types import ToolParam
from pydantic import BaseModel
from typing import Literal, Union, List
from helpers import lmk, setup_logging
import json
from constants import RAW_IMAGE_DIR

import logging

_logger = logging.getLogger(__name__)

MODEL = "claude-3-5-sonnet-20240620"
# MODEL = "claude-3-haiku-20240307"

# TODO: make smaller for $$
_SYSTEM_PROMPT = """\
This is transcript showing a helpful AI assistant determining whether the description, and other \
metadata about an image indicates that the image is of a flower. The user is trying to build a \
dataset of flower images, an ideal image is one that is of a single type of flower. The user \
wishes to use these images to get preference data between different types of flowers.

The assistant will only see json metadata about the image, and not the actual image. This is to \
do an early filter of the data for obvious non-flower images.

All the images were sourced by a search for "flowers" on Wikimedia Commons. But these will \
sometimes result in images with "rose" in the title, but not actually of a rose.

The assistant will not respond with text, however just make a function call to the submit_answer \
function, with the answer and also it's confidence level (high, medium, low).

The assistant will also provide a second answer, which is whether the image is of a single type of \
flower, or if it contains multiple types of flowers. For example, a description like "A bouquet of \
many flowers" would indicate multiple types of flowers. A confidence level should also be provided \
for this answer.

Finally, if the image is of a single type of flower, the assistant will provide the canonical \
common name and scientific name of the flower. If the image is of multiple types of flowers, \
the assistant will provide None for both the common name and scientific name.
"""

message_template = """\
Please determine if the image is of a flower, if it is of one or several types of flowers, and if \
it is just one, the canonical name, and scientific name (these can be the same if you like). The \
metadata is as follows (apologies for any formatting issues):

{metadata}\
"""

Confidence = Union[Literal["high"], Literal["medium"], Literal["low"]]


class SubmitAnswerModel(BaseModel):
    is_flower: bool
    is_flower_confidence: Confidence
    is_single_type_of_flower: bool
    is_single_type_of_flower_confidence: Confidence
    common_name: str
    scientific_name: str


class AiAnswerMetadataOnly(BaseModel):
    answer: SubmitAnswerModel
    metadata: dict
    uuid: str
    model: str


def _generate_message(metadata: dict) -> str:
    s = "\n".join([f"{k}: {v}" for k, v in metadata.items()])
    return message_template.format(metadata=s)


def _ask_claude(metadata: dict, client: Anthropic) -> SubmitAnswerModel:
    response = client.messages.create(
        system=_SYSTEM_PROMPT,
        model=MODEL,
        max_tokens=4096,
        messages=[{"role": "user", "content": _generate_message(metadata)}],
        tools=[
            ToolParam(
                name="submit_answer",
                input_schema=SubmitAnswerModel.model_json_schema(),
                description="Allows claude to submit an answer about the image metadata",
            ),
        ],
        tool_choice={"type": "tool", "name": "submit_answer"},
    )

    first_content = response.content[0]

    if first_content.type != "tool_use":
        raise ValueError("Claude did not respond with an answer")

    return SubmitAnswerModel.model_validate(first_content.input)


@lmk
def main_claude_metadata_only():
    client = Anthropic()
    all_responses: List[AiAnswerMetadataOnly] = []

    # iter all folders in the raw image directory
    for i, folder in enumerate(Path(RAW_IMAGE_DIR).iterdir()):
        try:
            if not folder.is_dir():
                continue

            # get metadata
            metadata_file = folder / "summary.json"

            if not metadata_file.exists():
                continue

            with open(metadata_file, "r") as f:
                metadata = json.load(f)

            # ask claude
            response = _ask_claude(metadata, client)
            all_responses.append(
                AiAnswerMetadataOnly(
                    answer=response, metadata=metadata, uuid=folder.name, model=MODEL
                )
            )

            if i % 10 == 0 and i > 0:
                with open("claude_metadata_only_responses.json", "w") as f:
                    json.dump([r.model_dump() for r in all_responses], f, indent=2)
        except Exception as e:
            _logger.error(f"Failed to process folder {folder}: {e}")


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    setup_logging("claude_metadata_only.log")
    main_claude_metadata_only()
