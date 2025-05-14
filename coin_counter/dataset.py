# coin-counter/dataset.py
from pathlib import Path


def load_image_label_pairs(image_dir, label_dir):
    image_paths = sorted(Path(image_dir).glob("*.jpg"))
    pairs = []
    for img_path in image_paths:
        label_path = Path(label_dir) / (img_path.stem + ".txt")
        if label_path.exists():
            pairs.append((img_path, label_path))
    return pairs
