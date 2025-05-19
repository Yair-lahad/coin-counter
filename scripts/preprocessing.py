from pathlib import Path
from PIL import Image
import shutil
import unicodedata

VALID_EXTENSIONS = {".jpg", ".jpeg", ".png"}

def normalize_name(name):
    return unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii').replace(" ", "_")

def flatten_and_fix_with_labels(source_image_dir, source_label_dir, target_image_dir, target_label_dir):
    source_image_dir = Path(source_image_dir)
    source_label_dir = Path(source_label_dir)
    target_image_dir = Path(target_image_dir)
    target_label_dir = Path(target_label_dir)

    target_image_dir.mkdir(parents=True, exist_ok=True)
    target_label_dir.mkdir(parents=True, exist_ok=True)

    counter = 0
    for img_path in source_image_dir.rglob("*"):
        if not img_path.is_file():
            continue
        if img_path.suffix.lower() not in VALID_EXTENSIONS:
            continue

        # Create safe new name
        rel_img_path = img_path.relative_to(source_image_dir)
        parts = rel_img_path.parts
        prefix = "_".join([normalize_name(p) for p in parts[:-1]])
        safe_stem = normalize_name(img_path.stem)
        new_base = f"{prefix}_{safe_stem}"
        new_image_name = f"{new_base}.jpg"
        new_label_name = f"{new_base}.txt"

        dest_image_path = target_image_dir / new_image_name
        dest_label_path = target_label_dir / new_label_name

        # Fix and copy image
        try:
            with Image.open(img_path) as img:
                rgb = img.convert('RGB')
                rgb.save(dest_image_path, "JPEG")
        except Exception as e:
            print(f"⚠️ Could not fix image: {img_path} — {e}")
            continue

        # Match label path from same relative structure under source_label_dir
        label_path = source_label_dir / rel_img_path.with_suffix('.txt')
        if label_path.exists():
            try:
                shutil.copy(label_path, dest_label_path)
            except Exception as e:
                print(f"⚠️ Could not copy label: {label_path} — {e}")
        else:
            print(f"⚠️ No label found for: {rel_img_path.with_suffix('.txt')}")

        counter += 1

    print(f"\n✅ Flattened and fixed {counter} image-label pairs.")
