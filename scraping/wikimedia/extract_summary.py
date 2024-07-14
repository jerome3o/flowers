# Extracts the summary section of a wikimedia page

from pathlib import Path
import os
import json
from bs4 import BeautifulSoup


_RAW_IMAGE_DIR = os.getenv("RAW_IMAGE_DIR", "./data/raw/images")


def extract_summary_content(html: str) -> dict:

    soup = BeautifulSoup(html, "html.parser")

    summary_sections = soup.find("div", class_="commons-file-information-table")
    summary_content = {}

    # this is a two column table, first column has a key, second value. Iterate over the rows
    # and extract the key-value pairs

    for row in summary_sections.find_all("tr"):

        row_items = list(row.find_all("td"))
        if len(row_items) != 2:
            continue

        key, value = row_items

        if key is not None and value is not None:
            key = key.text.strip()
            value = value.text.strip()

            summary_content[key] = value

    return summary_content


def main(folder_path: Path):

    for current_folder in folder_path.iterdir():
        if not current_folder.is_dir():
            continue

        html_file = current_folder / "metadata.html"

        with open(html_file, "r") as f:
            html = f.read()

        summary_content = extract_summary_content(html)

        # Save the summary content as a JSON file
        summary_file = current_folder / "summary.json"

        with open(summary_file, "w") as f:
            json.dump(summary_content, f, indent=4)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)

    # Usage example
    main(Path(_RAW_IMAGE_DIR))
