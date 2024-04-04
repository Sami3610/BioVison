from detect_blur_fft import detect_blur_fft
import numpy as np
import argparse
import imutils
import cv2
import os

input_folder = "D:/all_cambridge/09222023/images"
output_folder = "C:/Python-environments/blur.detection/output"

for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)

    # load the input image from disk, resize it, and convert it to
    # grayscale
    orig0 = cv2.imread(input_path, cv2.IMREAD_COLOR)
    orig = imutils.resize(orig0, width=800)
    #Converting the image to grayscale using
    gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
    # apply our blur detector using the Fast Fourier Transform
    (mean, blurry) = detect_blur_fft(gray, size=100,
	thresh=10, vis=-1)

    #dividing images according to Fast Fourier Transform amount
    if (blurry):
        folder_path = os.path.join(output_folder, "Blur.Images")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    else:
        folder_path = os.path.join(output_folder, "Clear.Images")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Modify the output path by adding the FFT to the filename
    filename_without_extension = os.path.splitext(filename)[0]
    #output_filename = f"{filename_without_extension}_FFT_{mean}.jpg"
    output_filename = f"_{mean}.jpg"
    output_path = os.path.join(folder_path, output_filename)

    # Save the image to the output folder
    cv2.imwrite(output_path, orig0, [cv2.IMWRITE_JPEG_QUALITY, 100])
    # Printing the filename and FFT amount
    print(f"Saved {output_filename} with FFT = {mean}")