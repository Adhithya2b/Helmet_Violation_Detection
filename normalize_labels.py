import os
from PIL import Image

labels_dir = 'dataset_split/train/labels'
images_dir = 'dataset_split/train/images'

for label_file in os.listdir(labels_dir):
    if not label_file.endswith('.txt'):
        continue
    label_path = os.path.join(labels_dir, label_file)
    image_name = os.path.splitext(label_file)[0]
    
    # Try both .png and .jpg
    img_path_png = os.path.join(images_dir, image_name + '.png')
    img_path_jpg = os.path.join(images_dir, image_name + '.jpg')
    
    if os.path.exists(img_path_png):
        img_path = img_path_png
    elif os.path.exists(img_path_jpg):
        img_path = img_path_jpg
    else:
        print(f"Image for {label_file} not found.")
        continue

    with Image.open(img_path) as img:
        w, h = img.size

    new_lines = []
    with open(label_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 5:
                continue
            cls, x, y, bw, bh = parts
            try:
                x, y, bw, bh = float(x) / w, float(y) / h, float(bw) / w, float(bh) / h
                # Check if within bounds (optional safety)
                if 0 <= x <= 1 and 0 <= y <= 1 and 0 <= bw <= 1 and 0 <= bh <= 1:
                    new_lines.append(f"{cls} {x} {y} {bw} {bh}")
            except ValueError:
                continue

    with open(label_path, 'w') as f:
        for newline in new_lines:
            f.write(newline + '\n')

print("Normalization complete.")
