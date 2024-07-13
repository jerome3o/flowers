import json
import uuid


def _make_uuid():
    return str(uuid.uuid4())


# {
#   "offset": 9990,
#   "data": [
#     [
#       {
#         "url": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Red_rose_with_black_background.jpg",
#         "descriptionurl": "https://commons.wikimedia.org/wiki/File:Red_rose_with_black_background.jpg",
#         "descriptionshorturl": "https://commons.wikimedia.org/w/index.php?curid=41380341"
#       }
#     ],
#     [
#       {
#         "url": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Englische_Rose_-The_Squire-_Raureif-20201107-RM-091853.jpg",
#         "descriptionurl": "https://commons.wikimedia.org/wiki/File:Englische_Rose_-The_Squire-_Raureif-20201107-RM-091853.jpg",
#         "descriptionshorturl": "https://commons.wikimedia.org/w/index.php?curid=96488040"
#       }
#     ],


def give_uuids(fn: str):
    with open(fn, "r") as f:
        data = json.load(f)

    for i in data["data"]:
        for j in i:
            # make uuid
            j["uuid"] = _make_uuid()

    with open(fn, "w") as f:
        json.dump(data, f, indent=2)


def make_dict(fn: str, output_fn: str):
    with open(fn, "r") as f:
        data = json.load(f)

    new_data = {}
    for i in data["data"]:
        for j in i:
            new_data[j["uuid"]] = j

    with open(output_fn, "w") as f:
        json.dump(new_data, f, indent=2)


def main():
    FILE_NAME = "./data/raw/info.json"
    DICT_FILE_NAME = "./data/raw/info_dict.json"
    # give_uuids(FILE_NAME)
    make_dict(FILE_NAME, DICT_FILE_NAME)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
