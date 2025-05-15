from ultralytics import YOLO

model = YOLO("yolov5s.pt")

model.train(
    data="coin.yaml",      # path to your YAML file
    epochs=10,
    imgsz=640,
    batch=4,
    name="v1",
    project="models/coin_detector",  # this controls the full save path,
    augment=True
)
