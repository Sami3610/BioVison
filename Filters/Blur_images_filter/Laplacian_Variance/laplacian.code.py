import cv2
import os

input_folder = ".........../input"
output_folder = "........../output"

for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    img = cv2.imread(input_path, cv2.IMREAD_COLOR)

    #Converting the image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Calculate laplacian variance
    laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()

    #dividing images according to laplacian_var
    if laplacian_var > 90:
        folder_path = os.path.join(output_folder, "Blur.Images")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    else:
        folder_path = os.path.join(output_folder, "Clear.Images")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Modify the output path by adding the laplacian_var to the filename
    filename_without_extension = os.path.splitext(filename)[0]
    
    output_filename = f"_lap_{laplacian_var}.jpg"
    output_path = os.path.join(folder_path, output_filename)

    # Save
    cv2.imwrite(output_path, img, [cv2.IMWRITE_JPEG_QUALITY, 100])
    
    print(f"Saved {output_filename} with laplacian_var = {laplacian_var}")