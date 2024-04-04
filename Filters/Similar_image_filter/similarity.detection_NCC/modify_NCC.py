import cv2
import numpy as np
import os
import shutil

# Define a search window size
window_size = (50, 50)  # Currently not used in the script

# Define a threshold NCC value
threshold_ncc = 0.9

# Load the images
image_folder = '............/dataset'
image_filenames = os.listdir(image_folder)
images = []
for filename in image_filenames:
    image = cv2.imread(os.path.join(image_folder, filename), cv2.IMREAD_GRAYSCALE)
    # Resize the image to 256x146 to speed up computation
    resized_image = cv2.resize(image, (256, 146))
    images.append(resized_image)

# Compute the NCC between pairs of images
n_images = len(images)
ncc_values = np.zeros((n_images, n_images))
for i in range(n_images):
    for j in range(n_images):
        if i != j:
            result = cv2.matchTemplate(images[i], images[j], cv2.TM_CCOEFF_NORMED)
            ncc_values[i, j] = np.max(result)
            # Print the NCC value for every comparison
            print(f'NCC between {image_filenames[i]} and {image_filenames[j]}: {ncc_values[i, j]:.2f}')

# Find the most similar images
similar_images = []
for i in range(n_images):
    for j in range(i + 1, n_images):
        if ncc_values[i, j] > threshold_ncc:
            similar_images.append((i, j, ncc_values[i, j]))

# Create a folder to store similar images
output_folder = '................../Removed_images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Move the similar images to the output folder
for i, j, ncc in similar_images:
    image_i_path = os.path.join(image_folder, image_filenames[i])
    image_j_path = os.path.join(image_folder, image_filenames[j])
    output_i_path = os.path.join(output_folder, image_filenames[i])
    output_j_path = os.path.join(output_folder, image_filenames[j])
    if not os.path.exists(output_i_path):
        shutil.move(image_i_path, output_folder)
    if not os.path.exists(output_j_path):
        shutil.move(image_j_path, output_folder)
    print(f'Moved similar images: {image_filenames[i]}, {image_filenames[j]} with NCC: {ncc:.2f}')
