from pathlib import Path
import shutil

VALID_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def flatten_images(source_dir, target_dir="data/images"):
    """
    Copies up to max_files valid images from a directory tree into a flat folder.
    Renames each image based on its subfolder path.
    """
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    counter = 0
    for img_path in source_dir.rglob("*"):
        if not img_path.is_file():
            continue
        if img_path.suffix.lower() not in VALID_EXTENSIONS:
            continue

        parts = img_path.relative_to(source_dir).parts
        prefix = "_".join(parts[:-1])
        new_name = f"{prefix}_{img_path.stem}.jpg"
        dest_path = target_dir / new_name

        if not dest_path.exists():
            shutil.copy(img_path, dest_path)
            counter += 1

    print(f"Flattened {counter} images to {target_dir}")
