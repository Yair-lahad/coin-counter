from preprocessing import flatten_and_fix_with_labels

flatten_and_fix_with_labels(
    source_image_dir="data/images/train_pre",
    source_label_dir="data/labels/train_pre",
    target_image_dir="data/images/train",
    target_label_dir="data/labels/train"
)
flatten_and_fix_with_labels(
    source_image_dir="data/images/val_pre",
    source_label_dir="data/labels/val_pre",
    target_image_dir="data/images/val",
    target_label_dir="data/labels/val"
)