import os


NTFY_TOPIC = os.getenv("NTFY_TOPIC")
JSON_FILE_PATH = os.getenv("INFO_DICT_PATH", "./data/raw/info_dict.json")
RAW_IMAGE_DIR = os.getenv("RAW_IMAGE_DIR", "./data/raw/images")

# for hostname try read /etc/hostname
try:
    with open("/etc/hostname") as f:
        HOSTNAME = f.read().strip()
except Exception:
    HOSTNAME = os.getenv("HOSTNAME", "localhost")
