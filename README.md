# Helmet Violation Detection

A computer vision project for detecting helmet violations using YOLOv5.


## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Check GPU availability:
```bash
python gpuCheck.py
```

3. Prepare the dataset:
```bash
# Convert annotations to YOLO format
python formatting.py

# Split dataset into train and validation sets
python splitting.py

# Normalize label coordinates
python normalize_labels.py
```

4. Train the model:
```bash
cd yolov5
python train.py --img 640 --batch 4 --epochs 5 --data ../helmet.yaml --weights yolov5n.pt --device 0
```

Training parameters:
- Image size: 640x640
- Batch size: 4
- Epochs: 5
- Base model: YOLOv5n
- Device: GPU (device 0)

## Detection

To detect helmets in images:
```bash
python detect.py --weights runs/train/exp7/weights/best.pt --img 640 --conf 0.25 --source trail1.png
```

Detection parameters:
- Model weights: best.pt from exp7
- Image size: 640x640
- Confidence threshold: 0.25
- Source: trail1.png

## Model Training

The model is trained on a custom dataset for helmet detection with two classes:
- With Helmet
- Without Helmet

## Dataset Preparation

The project includes several utility scripts for dataset preparation:

1. `formatting.py`: Converts annotations from the original format to YOLO format
2. `gpuCheck.py`: Verifies CUDA availability and displays GPU information
3. `splitting.py`: Splits the dataset into training (80%) and validation (20%) sets
4. `normalize_labels.py`: Normalizes bounding box coordinates in label files to be relative to image dimensions

## Results

The trained model will be saved in `runs/train/exp7/weights/`:
- `best.pt`: Best model based on validation performance
- `last.pt`: Latest model weights
