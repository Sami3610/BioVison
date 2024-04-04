import os
import shutil
from PIL import Image
import numpy as np

source_folder = "............../input"
duplicate_folder = "........../output"

mse_threshold = 45
images = []
min_mse_for_image = {}

# Read and store all images
for filename in os.listdir(source_folder):
    if not filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
        continue

    img = Image.open(os.path.join(source_folder, filename))
    new_size = (256, 146)
    img = img.resize(new_size)
    img = img.convert("L")
    pixel_array = np.array(img)
    images.append((filename, pixel_array))

    min_mse_for_image[filename] = float('inf')

# Compare images and calculate MSE
for i in range(len(images)):
    for j in range(i+1, len(images)):
        mse = np.mean((images[i][1] - images[j][1])**2)

        # Print the filenames and MSE
        print(f"Comparing {images[i][0]} and {images[j][0]}: MSE = {mse}")

        if mse < min_mse_for_image[images[i][0]]:
            min_mse_for_image[images[i][0]] = mse
        if mse < min_mse_for_image[images[j][0]]:
            min_mse_for_image[images[j][0]] = mse

# Rename files with their minimum MSE
for filename, mse in min_mse_for_image.items():
    src_path = os.path.join(source_folder, filename)
    if os.path.exists(src_path):
        base_name, ext = os.path.splitext(filename)
        new_filename = f"{base_name}.{int(mse)}{ext}"
        dest_path = os.path.join(source_folder, new_filename)
        os.rename(src_path, dest_path)

# Move duplicates if MSE is below the threshold
for i in range(len(images)):
    for j in range(i+1, len(images)):
        mse = np.mean((images[i][1] - images[j][1])**2)
        if mse < mse_threshold:
            duplicate_filename = images[j][0]
            src_path = os.path.join(source_folder, duplicate_filename)
            base_name, ext = os.path.splitext(duplicate_filename)
            new_filename = f"{base_name}.{int(mse)}{ext}"
            duplicate_path = os.path.join(duplicate_folder, new_filename)
            if not os.path.exists(duplicate_path) and os.path.exists(src_path):
                shutil.move(src_path, duplicate_path)
