import os
import glob
import pandas as pd
from ultralytics import YOLO

COIN_VALUE_MAP = {
    "One": 1,
    "Two": 2,
    "Five": 5,
    "Ten": 10
}


def predict_and_sum(image_path, model):
    results = model(image_path)[0]
    total = 0
    detected = []
    for box in results.boxes:
        cls_id = int(box.cls.item())
        class_name = model.names[cls_id]
        conf = float(box.conf.item())
        value = COIN_VALUE_MAP.get(class_name, 0)
        total += value
        detected.append((class_name, conf))
    return total, os.path.basename(image_path), detected


def main():
    model = YOLO("models/shared/best.pt")
    image_dir = "data/unlabeled"
    image_paths = sorted(glob.glob(os.path.join(image_dir, "*.*")))
    if not image_paths:
        print(f"No images found in {image_dir}")
        return
    rows = []
    for image_path in image_paths:
        total, filename, detected = predict_and_sum(image_path, model)
        coins = ", ".join([f"{name} ({conf:.2f})" for name, conf in detected])
        rows.append({"Image": filename, "Coins": coins, "Total NIS": total})
    df = pd.DataFrame(rows)
    df.to_csv("coin_summary.csv", index=False)
    print(df)


if __name__ == "__main__":
    main()
