import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from video_cv_service.video_loop import cv_loop
from video_cv_service.config import get_config_from_dotenv
from video_cv_service.image_files_utils import clear_images_dir

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(
        format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
        datefmt="%H:%M:%S %d.%m.%Y",
        level=logging.DEBUG
    )

    config: dict | None = get_config_from_dotenv()
    if config is None:
        logging.error("Произошла ошибка при конфигурации приложения. Выход...")
        return

    out: Path = Path(config["IMAGES_DIRECTORY_PATH"])
    if out.exists() and out.is_dir():
        clear_images_dir(out)
    else:
        out.mkdir(parents=True, exist_ok=True)
        logger.info("Создана директория для изображений %s", str(out.resolve()))

    cv_loop(video_address=config["VIDEO_ADDRESS"],
            capture_interval=config["CAPTURE_INTERVAL"],
            window_name="Camera Image",
            out_directory=out)


if __name__ == "__main__":
    main()
