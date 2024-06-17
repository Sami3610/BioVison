# Blur images Detection using Laplacian Variance

In the realm of digital imaging, clarity is key. However, images, especially those captured in dynamic environments, often suffer from varying degrees of blurriness. Addressing this, the Laplacian Variance technique stands out as a reliable metric for assessing image quality, particularly in terms of blur. By employing the Laplacian operator—a second-order derivative method that accentuates rapid intensity changes indicative of edges—this technique calculates the variance of the Laplacian to effectively highlight areas of blur in images.

## Overview

This script utilizes the Laplacian Variance method to sift through a dataset of images, categorizing them based on their clarity. Images are classified as either "Blur" or "Clear", depending on their Laplacian variance value, and are then saved into corresponding subfolders within an output directory. This automated process not only streamlines the task of identifying blur in images but also organizes them for ease of analysis and further processing.

## Getting Started

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.6 or later
- OpenCV library

The OpenCV library can be installed via pip:

```bash
pip install opencv-python
```

## Installation

1. Clone or download this repository to your local machine.
2. Update the input_folder and output_folder variables in the script to point to your specific directories.

## Running the Script

To execute the script, navigate to the directory containing the script in your terminal or command prompt and run:

```bash
python laplacian.code.py
```

The script processes each image in the input_folder, applying the Laplacian Variance technique to determine the level of blur. Based on the calculated Laplacian variance, images are sorted into "Blur.Images" or "Clear.Images" within the output_folder.

## Output

The script saves each image into the appropriate subfolder, appending the calculated Laplacian variance to the filename for reference. This facilitates a quick review of the blur assessment for each image.

|           |Images                    |Laplacian Variance Value|
|-----------|--------------------------|------------------------|
|Blur Image |![1](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/B1.jpg)|LP=66.89|
|Blur Image |![2](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/B2.jpg) |LP=72.39|
|Blur Image |![3](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/B3.jpg)|LP=111.06|
|Clear Image|![4](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/B4.jpg) |LP=87.18 |
|Clear Image|![5](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/B5.jpg)|LP=669.03|
|Clear Image|![6](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/B6.jpg)|LP=1100.78|

## Contributing

Contributions to improve the Laplacian Variance blur detection script are welcome. Feel free to fork the repository, make your enhancements, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file in the repository for more details.

## Acknowledgments

- Kudos to the developers and contributors of the OpenCV library for providing the essential tools used in this project.