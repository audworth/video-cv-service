import zipfile
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def zip_images(dir: Path, zip_name: str) -> None:
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in dir.iterdir():
            if file.is_file():
                zipf.write(file, arcname=file.name)
    logger.info(f"Файлы архивированы в {zip_name}")


def clear_images_dir(dir: Path) -> None:
    for file in dir.iterdir():
        if file.is_file():
            file.unlink()
    logger.info("Директория с изображениями очищена")
