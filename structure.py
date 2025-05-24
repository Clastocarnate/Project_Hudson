import os
import shutil
import random
from pathlib import Path

# Set random seed for reproducibility
random.seed(42)

# Define source directories
images_dir = Path('Datasets')
labels_dir = Path('test_Labels')

# Define destination directories
dataset_dir = Path('dataset')
train_images_dir = dataset_dir / 'train' / 'images'
train_labels_dir = dataset_dir / 'train' / 'labels'
val_images_dir = dataset_dir / 'val' / 'images'
val_labels_dir = dataset_dir / 'val' / 'labels'

# Create destination directories
for directory in [train_images_dir, train_labels_dir, val_images_dir, val_labels_dir]:
    directory.mkdir(parents=True, exist_ok=True)

# Get list of image files
image_files = list(images_dir.glob('*.jpeg'))

# Filter image files that have corresponding label files
matched_files = []
for image_path in image_files:
    label_path = labels_dir / (image_path.stem + '.txt')
    if label_path.exists():
        matched_files.append((image_path, label_path))

# Shuffle and split into train and validation sets (80% train, 20% val)
random.shuffle(matched_files)
split_index = int(0.8 * len(matched_files))
train_files = matched_files[:split_index]
val_files = matched_files[split_index:]

# Function to copy files to destination
def copy_files(file_list, images_dest, labels_dest):
    for img_path, lbl_path in file_list:
        shutil.copy(img_path, images_dest / img_path.name)
        shutil.copy(lbl_path, labels_dest / lbl_path.name)

# Copy training files
copy_files(train_files, train_images_dir, train_labels_dir)

# Copy validation files
copy_files(val_files, val_images_dir, val_labels_dir)

# Create data.yaml file
data_yaml_content = f"""
path: {dataset_dir}
train: train/images
val: val/images
nc: 1
names: ['Ayush']
"""

with open(dataset_dir / 'data.yaml', 'w') as f:
    f.write(data_yaml_content.strip())

print("Dataset preparation is complete.")
