from ultralytics import YOLO
import shutil
import os


model = YOLO("yolov8n.pt")  # Load YOLOv8 model

# Train the model with heavy augmentations and backbone freezing
model.train(
    data="coin.yaml",              # path to dataset yaml
    epochs=30,
    patience=10,  # stop if no improvement after k epochs
    imgsz=768,
    batch=7,
    name="v1",
    project="models/coin_detector",
    freeze=0,                     # freeze first k layers (backbone)
    # flipud=0.2,
    # fliplr=0.5,
    # mosaic=0.5,
    # hsv_h=0.005,
    # hsv_s=0.3,
    # hsv_v=0.2
)

src = "models/coin_detector/v1/weights/best.pt"
dst = "models/shared/best.pt"

if not os.path.exists(dst):
    shutil.copy(src, dst) # Copy the file if it doesn't exist
