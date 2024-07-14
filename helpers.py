from constants import NTFY_TOPIC, HOSTNAME
import logging
import requests


def setup_logging(file_name: str | None = None):
    file_name = file_name or "flowers_general.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("file_name"),
            logging.StreamHandler(),
        ],
    )


def _ping_ntfy(message: str):
    requests.post(
        f"https://ntfy.sh/{NTFY_TOPIC}",
        data=message,
    )


def lmk(f):
    def wrapper(*args, **kwargs):

        # get function name
        name = f.__name__

        _ping_ntfy(f"🚦 {HOSTNAME} - {name} started")

        try:

            output = f(*args, **kwargs)
        except Exception as e:
            _ping_ntfy(f"🚨 {HOSTNAME} - {name} failed with error: {e}")
            raise e

        _ping_ntfy(f"🎉 {HOSTNAME} - {name} succeeded")

        return output

    return wrapper
