import shutil
import os
from pathlib import Path

# Define paths to clean
model_dir = Path("models/coin_detector/v1")
predict_dir = Path("results/model_labels/v1")
train_cache = Path("data/labels/train.cache")
val_cache = Path("data/labels/val.cache")

# Delete model output
if model_dir.exists():
    print(f"Deleting {model_dir}")
    shutil.rmtree(model_dir)

# Delete prediction output
if predict_dir.exists():
    print(f"Deleting {predict_dir}")
    shutil.rmtree(predict_dir)

# Delete training cache files
for cache_path in [train_cache, val_cache]:
    if cache_path.exists():
        print(f"Deleting {cache_path}")
        cache_path.unlink()

print("Cleanup completed.")
