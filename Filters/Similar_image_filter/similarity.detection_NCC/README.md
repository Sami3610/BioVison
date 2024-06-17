# Normalized Cross-Correlation Technique for Similar Images

Normalized Cross-Correlation (NCC) is a powerful statistical method utilized in image processing to measure the similarity between two images. Unlike other methods that might solely rely on pixel intensity differences, NCC takes into account the pattern of pixel intensity, offering a more nuanced comparison especially beneficial for identifying nearly identical images within a dataset. This Python script employs the NCC technique to scan through a collection of images, calculating the NCC value for each pair. Images yielding an NCC value above a specified threshold are flagged as similar. Such images are subsequently moved to a designated output directory, significantly aiding in the refinement of image datasets by effectively segregating closely matching images.

## Getting Started

Follow these instructions to implement the NCC Image Filter in your development and testing environments.

## Prerequisites

Ensure Python (version 3.6 or later) is installed on your system. This script relies on the following Python libraries:

- OpenCV (cv2)
- NumPy

You can install these dependencies using pip:

```bash
pip install opencv-python numpy
```

## Installation

- Download or clone the repository containing the script.
- Update the image_folder and output_folder paths in the script to correspond with your local directories.

## Configuration

- image_folder: The directory containing the images to analyze.
- output_folder: The location to store images deemed similar based on the NCC threshold.
- threshold_ncc: The NCC value above which two images are considered similar. The default value is set to 0.9.

## Running the Script
To run the script, use the following command in your terminal or command prompt:

```bash
python modify_NCC.py
```

The script processes all images in the image_folder, compares them, and relocates the similar ones to the output_folder.

## Example Output

Upon execution, images identified as similar are moved to the output_folder. The script also prints the NCC values for each image comparison:

|   |Image 1|&|Image 2|NCC Value|
|---|-------|-|-------|---------|
|A|![1](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepA1.jpg)|AND|![2](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepA2.jpg)| NCC Value=0.97|
|B|![3](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepB1.jpg)|AND|![4](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepB2.jpg)| NCC Value=0.8 |
|C|![5](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepC1.jpg)|AND|![6](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepC2.jpg)| NCC Value=0.9 |
|D|![7](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepD1.jpg)|AND|![8](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepD2.jpg)| NCC Value=0.09|

## Contributing

We encourage contributions to enhance the NCC Image Filter. If you have suggestions or improvements, please fork the repository, apply your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Special thanks to contributors and the Python community for their support and contributions to this project.
- Inspired by the challenges of maintaining high-quality image datasets in machine learning and data analytics.
