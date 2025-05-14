from helpers.preprocessing import flatten_images
from pathlib import Path

if __name__ == "__main__":
    root = Path("C:/raw_coin_images")
    VALID_EXTENSIONS = {".jpg", ".jpeg", ".png"}

    all_subdirs = [p for p in root.rglob("*") if p.is_dir()]
    all_valid_dirs = [p for p in all_subdirs if any(
        f.suffix.lower() in VALID_EXTENSIONS for f in p.iterdir())]

    print(f"Found {len(all_valid_dirs)} image folders")

    for folder in all_valid_dirs:
        flatten_images(folder, target_dir="data/images")
