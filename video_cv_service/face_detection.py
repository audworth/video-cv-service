import time
import logging
from pathlib import Path
from datetime import datetime
from typing import Tuple, List
import cv2

logger = logging.getLogger(__name__)


def detect_faces(
    face_detector: cv2.CascadeClassifier,
    gray_img
) -> List[Tuple[int, int, int, int]]:
    return face_detector.detectMultiScale(gray_img,
                                          scaleFactor=1.3,
                                          minNeighbors=5)


def save_detected_faces(
    img,
    faces: List[Tuple[int, int, int, int]],
    out_directory: Path,
    timestamp: float
) -> None:
    for (x, y, w, h) in faces:
        face_img = img[y:y+h, x:x+w]
        now: str = datetime.fromtimestamp(timestamp) \
                           .strftime("%H-%M-%S-%d-%m-%Y")
        file_name: str = f"{now}.jpg"
        cv2.imwrite(str(out_directory / file_name), face_img)
        logger.info("Сохранено изображение: %s в %s", file_name, str(out_directory.resolve()))


def process_video_frame(
    img,
    face_detector: cv2.CascadeClassifier,
    last_saved_time: float,
    capture_interval: float,
    out_directory: Path
) -> float:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detect_faces(face_detector, gray)

    current_time: float = time.time()
    if len(faces) > 0 and current_time - last_saved_time >= capture_interval:
        save_detected_faces(img, faces, out_directory, current_time)
        last_saved_time = current_time

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return last_saved_time
