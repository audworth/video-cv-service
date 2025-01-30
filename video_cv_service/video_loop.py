import cv2
import time
import logging
from pathlib import Path
from face_detection import process_video_frame

logger = logging.getLogger(__name__)


def cv_loop(
    video_address: int | str,
    capture_interval: float,
    window_name: str,
    out_directory: Path
) -> None:
    face_detector = cv2.CascadeClassifier(
        "../cascades/haarcascade_frontalface_default.xml"
    )

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    last_saved_time = time.time()
    vid = cv2.VideoCapture(video_address)
    logger.info("Открытие видеопотока...")

    try:
        while True:
            ret, img = vid.read()
            if not ret:
                logger.error("Не обнаружено кадров видеопотока")
                break

            last_saved_time = process_video_frame(img,
                                                  face_detector,
                                                  last_saved_time,
                                                  capture_interval,
                                                  out_directory)

            cv2.imshow(window_name, img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        vid.release()
        cv2.destroyAllWindows()
        logger.warning("Видеопоток закрыт")
