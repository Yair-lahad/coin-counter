from ultralytics import YOLO
from pathlib import Path

model = YOLO("models/coin_detector/v1/weights/best.pt")
# Resolve path relative to this script
image_folder = Path(__file__).resolve().parents[1] / "data/unlabeled"

model.predict(
    source=str(image_folder),
    save=True,
    save_txt=True,
    project="results/model_labels",
    name="v1",
    imgsz=640
)
