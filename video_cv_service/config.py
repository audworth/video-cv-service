import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def get_config_from_dotenv() -> dict | None:
    load_dotenv("./.env")
    config: dict = {
        "VIDEO_ADDRESS": (
            int(os.getenv("VIDEO_ADDRESS"))
            if (
                os.getenv("VIDEO_ADDRESS")
                and os.getenv("VIDEO_ADDRESS").isdigit()
                and len(os.getenv("VIDEO_ADDRESS")) == 1
            )
            else os.getenv("VIDEO_ADDRESS")
        ),
        "CAPTURE_INTERVAL": (
            int(os.getenv("CAPTURE_INTERVAL"))
            if (
                os.getenv("CAPTURE_INTERVAL")
                and os.getenv("CAPTURE_INTERVAL").isdigit()
            )
            else None
        ),
        "IMAGES_DIRECTORY_PATH": os.getenv("IMAGES_DIRECTORY_PATH"),
    }

    if any(value is None for value in config.values()):
        missing: dict = [key for key, value in config.items() if value is None]
        logging.error("Следующие переменные окружения инициализированы неверно: %s", ', '.join(missing))
        return None

    return config
