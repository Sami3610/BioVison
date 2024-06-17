# Blur images Detection using Fast Fourier Transform (FFT)

The Fast Fourier Transform (FFT) stands as a cornerstone technique in digital image processing, particularly in the realm of blur detection. This method transforms an image from its spatial domain to the frequency domain, allowing for the analysis of frequency components. Since blurred images are characterized by a lack of high-frequency elements—markers of sharp edges and intricate details—FFT serves as an effective tool to distinguish between clear and blurred images by assessing their frequency spectra.

## Overview

This folder contains a script that applies the FFT to automatically identify blurred images within a dataset. By analyzing the frequency components and identifying images with insufficient high-frequency content, the script can efficiently segregate blurred images from those that are clear. This process facilitates the preparation of image datasets by ensuring only high-quality, clear images are retained for further processing or analysis.

## Getting Started

## Prerequisites

- Python 3.6 or newer
- OpenCV
- Imutils
- NumPy
- Matplotlib (optional, for visualization)

You can install the required libraries using pip:

"pip install opencv-python imutils numpy matplotlib"

## Installation

1. Clone or download this repository to your local environment.
2. ** Ensure the detect_blur_fft.py script is placed within an accessible directory.**
3. Update the input_folder and output_folder paths in the script to point to your directories.

## Running the Script

Execute the script from your terminal or command prompt:

"python modified_fft.code.py"

This script processes each image in the input_folder, applies FFT to determine the blur level based on the defined threshold, and sorts the images into "Blur.Images" or "Clear.Images" within the output_folder, appending the FFT mean value to the filename for easy reference.

## Understanding the Output

The script outputs each image into the designated subfolder, classifying them based on their blur status. The FFT mean value is included in the filename, providing immediate insight into the blur level assessed for each image.

|           |Images                    |FFT Value|
|-----------|--------------------------|----------|
|Blur Image |(https://github.com/Sami3610/BioVison/blob/main/Filters/Images/B1.jpg) |FFT=-1.46 |
|Blur Image |(https://github.com/Sami3610/BioVison/blob/main/Filters/Images/B2.jpg) |FFT=-10.21|
|Blur Image |(https://github.com/Sami3610/BioVison/blob/main/Filters/Images/B3.jpg) |FFT=-13.49|
|Clear Image|(https://github.com/Sami3610/BioVison/blob/main/Filters/Images/B4.jpg) |FFT=19.22 |
|Clear Image|(https://github.com/Sami3610/BioVison/blob/main/Filters/Images/B5.jpg) |FFT=31.8  |
|Clear Image|(https://github.com/Sami3610/BioVison/blob/main/Filters/Images/B6.jpg) |FFT=41.64 |

## Contributing

We welcome contributions, improvements, and bug fixes. Feel free to fork the repository, make your changes, and submit a pull request for review.

## License

This project is licensed under the MIT License - see the LICENSE.md file for more details.

## Acknowledgments

- Appreciation to the developers of the Python libraries used in this project, facilitating the advanced processing of image data.
