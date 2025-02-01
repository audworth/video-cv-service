import logging
from pathlib import Path
from video_cv_service.video_loop import cv_loop
from video_cv_service.image_files_utils import clear_images_dir

logger = logging.getLogger(__name__)


def main() -> None:
    out: Path = Path("./imgs/")

    logging.basicConfig(
        format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
        datefmt="%d.%m.%Y %H:%M:%S",
        level=logging.DEBUG
    )

    if out.exists() and out.is_dir():
        clear_images_dir(out)
    else:
        out.mkdir(parents=True, exist_ok=True)
        logger.info("Создана директория для изображений %s", str(out.resolve()))

    # 0 - веб камера
    cv_loop(video_address=0,
            capture_interval=3,
            window_name="Camera Image",
            out_directory=out)


if __name__ == "__main__":
    main()
