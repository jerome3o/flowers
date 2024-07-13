import json
import requests
import os
from pathlib import Path
import time
from urllib.parse import urlparse
import logging


_logger = logging.getLogger(__name__)


WIKIMEDIA_ACCESS_TOKEN = os.environ["WIKIMEDIA_ACCESS_TOKEN"]


def fetch_and_save_images(json_file_path, output_dir):
    # Ensure output directory exists
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Read the JSON file
    with open(json_file_path, "r") as f:
        data = json.load(f)

    headers = {
        "User-Agent": "FlowerImageFetcher/1.0 (jeromeswannack@gmail.com)",
        "Authorization": f"Bearer {WIKIMEDIA_ACCESS_TOKEN}",
    }

    for uuid, item in data.items():
        image_url = item["url"]
        metadata_url = item["descriptionurl"]

        # Create subdirectory for each UUID
        uuid_dir = output_dir / uuid
        uuid_dir.mkdir(exist_ok=True)

        # Fetch and save image
        image_response = requests.get(image_url, headers=headers)
        if image_response.status_code == 200:
            image_extension = os.path.splitext(urlparse(image_url).path)[1]
            with open(uuid_dir / f"image{image_extension}", "wb") as f:
                f.write(image_response.content)
            _logger.info(f"Saved image for {uuid}")
        else:
            _logger.warning(f"Failed to fetch image for {uuid}")

        # Fetch and save metadata
        metadata_response = requests.get(metadata_url, headers=headers)
        if metadata_response.status_code == 200:
            with open(uuid_dir / "metadata.html", "w", encoding="utf-8") as f:
                f.write(metadata_response.text)
            _logger.info(f"Saved metadata for {uuid}")
        else:
            _logger.warning(f"Failed to fetch metadata for {uuid}")

        # Save original JSON data
        with open(uuid_dir / "info.json", "w") as f:
            json.dump(item, f, indent=2)

        # Be nice to the server
        time.sleep(1)


if __name__ == "__main__":

    # logger that writes to file and console
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("fetch_images.log"),
            logging.StreamHandler(),
        ],
    )

    json_file_path = "./data/raw/info_dict.json"
    output_dir = "./data/raw/images"
    fetch_and_save_images(json_file_path, output_dir)