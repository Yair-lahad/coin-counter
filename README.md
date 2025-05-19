# Coin Counter

A computer vision system that detects and counts Israeli coins in an image, calculating the total monetary value.

## Project Overview

This project implements an object detection system that:
1. Identifies Israeli coins (₪1, ₪2, ₪5, ₪10) in images
2. Calculates the total monetary value of all detected coins
3. return CSV of results

## Dataset

The system is trained on a custom dataset of Israeli coins:

- **Classes**: Four coin denominations
  - 1 Shekel ("One")
  - 2 Shekels ("Two")
  - 5 Shekels ("Five")
  - 10 Shekels ("Ten")
- **Size**: 50+ images with various:
  - Backgrounds
  - Lighting conditions
  - Angles
  - Coin arrangements
- Dataset is split into training and testing sets

## Model Architecture

The project uses Ultralytics with YOLOv8, a state-of-the-art object detection model:
- Base model: YOLOv8n (nano variant)
- Transfer learning with freeze layers
- Custom training with data augmentation

### Data Preparation and Notes

- You must include model file "best.pt" at location: models/shared/best.pt in order to run the model successfuly.
- You must include coin.yaml (included in git)

Prepare your data for training:
add images to data/images/train + data/images/val
add YOLO labels to data/labels/train + data/labels/val
add unlabeled images for prediction to data/unlabeled

read more at: https://docs.ultralytics.com/datasets/detect/#ultralytics-yolo-format

## Project Structure

```
coin-counter/
├── coin_counter/           # Main package
│   ├── __init__.py
│   ├── predict.py          # Run predictions on unlabeled images
│   └── train.py            # Model training script
├── data/                   # Dataset storage
│   ├── images/             # Image data
│   │   ├── train/          # Training images (processed)
│   │   ├── val/            # Validation images (processed)
│   ├── labels/             # YOLO format annotations
│   │   ├── train/          # Training labels (processed)
│   │   ├── val/            # Validation labels (processed)
│   └── unlabeled/          # Images for inference
├── models/                 # Trained model storage
│   ├── coin_detector/      # Training results
│   └── shared/             # Shared model weights
├── results/                # Prediction outputs
│   └── model_labels/       # Labeled prediction images
├── scripts/                # Utility scripts
│   ├── cleanup.py          # Clean cache and results
│   ├── coin_counter.py     # Run inference and calculate totals
│   ├── preprocessing.py    # Data preprocessing utilities
│   └── prepare_data.py     # Prepare data for training
├── coin.yaml               # Dataset configuration
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/Yair-lahad/coin-counter.git
cd coin-counter
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage
See Data Preparation and Notes section prior to usage run.

### prepare images and label files
```bash
python scripts/prepare_data.py
```

### Training

Train the coin detection model:
```bash
python coin_counter/train.py
```

### Inference
if needed run a prediction to see results of object detection:
```bash
python coin_counter/predict.py
```

Run the model on new images and calculate total coin value:
```bash
python scripts/coin_counter.py
```

### Cleanup

Clean up cache and temporary files:
```bash
python scripts/cleanup.py
```


## Future Improvements

- Evaluation
- Expand dataset with more images in varied conditions
- Test different model architectures
- Implement handling of overlapping coins
- Add real-time detection using webcam feed

