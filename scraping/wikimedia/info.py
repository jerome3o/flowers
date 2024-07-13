import requests
import json
import time
import urllib
import os
from pathlib import Path


WIKIMEDIA_ACCESS_TOKEN = os.environ["WIKIMEDIA_ACCESS_TOKEN"]


def _get_full_url(base_url: str, params: dict):
    # Encode the parameters
    encoded_params = urllib.parse.urlencode(params)

    # Combine the base URL with the encoded parameters
    return f"{base_url}?{encoded_params}"


def _print_full_url(base_url: str, params: dict):
    print(_get_full_url(base_url, params))


def get_flower_images(
    output_fn="data/raw/info.json",
    search_term="flower",
    total_limit=100,
    batch_size=50,
):
    output_path = Path(output_fn)
    output_path.parent.mkdir(exist_ok=True, parents=True)
    base_url = "https://commons.wikimedia.org/w/api.php"

    # Define headers
    headers = {
        "User-Agent": "FlowerImageFetcher/1.0 (jeromeswannack@gmail.com)",
        "Accept": "application/json",
        "Authorization": f"Bearer {WIKIMEDIA_ACCESS_TOKEN}",
    }

    all_image_info = []
    offset = 0

    while len(all_image_info) < total_limit:
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": f"{search_term} filetype:bitmap",
            "srnamespace": "6",  # File namespace
            "srlimit": min(batch_size, total_limit - len(all_image_info)),
            "sroffset": offset,
        }

        _print_full_url(base_url, params)
        response = requests.get(base_url, params=params, headers=headers).json()
        print(response)

        if "query" not in response or "search" not in response["query"]:
            break  # No more results

        image_titles = [item["title"] for item in response["query"]["search"]]

        for title in image_titles:
            file_params = {
                "action": "query",
                "format": "json",
                "prop": "imageinfo",
                "iiprop": "url",
                "titles": title,
            }
            _print_full_url(base_url, file_params)
            file_response = requests.get(
                base_url, params=file_params, headers=headers
            ).json()
            pages = file_response["query"]["pages"]
            for page in pages.values():
                if "imageinfo" in page:
                    all_image_info.append(page["imageinfo"])
                    if len(all_image_info) >= total_limit:
                        return all_image_info

        offset += len(image_titles)

        with open(output_path, "w") as f:
            json.dump({"offset": offset, "data": all_image_info}, f)

        time.sleep(0.5)  # Be nice to the API

    return all_image_info


# Example usage
flower_images = get_flower_images(search_term="rose", total_limit=10000, batch_size=10)
for i, url in enumerate(flower_images, 1):
    print(f"{i}. {url}")

print(f"\nTotal images fetched: {len(flower_images)}")
