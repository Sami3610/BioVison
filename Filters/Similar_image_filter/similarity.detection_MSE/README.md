# The Mean Square Error technique for similar images

Mean Squared Error (MSE) is widely recognized as a robust measure for assessing signal fidelity and similarity in image analysis, providing a quantitative score to evaluate the error or likeness between two images. Typically, in this context, one image serves as the reference or original, while the comparison involves a distorted or altered counterpart. Leveraging the MSE technique, this Python script is designed to meticulously identify and segregate similar images within a dataset. By meticulously comparing the pixel values of image pairs, it quantifies their similarity through MSE calculations. When the MSE falls below a predetermined threshold, the images are deemed duplicates. Such images are then relocated to a designated output directory, significantly streamlining the process of dataset cleansing by efficiently removing or isolating nearly identical images. This approach not only enhances dataset quality but also aids in the effective management and utilization of image data.

## Getting Started

These instructions will guide you on how to deploy the MSE Image Filter in your local environment for both development and testing purposes.

### Prerequisites

Ensure you have Python installed (version 3.6 or newer is recommended). The script depends on the following Python packages

- Pillow (PIL Fork)
- NumPy

Install these packages using pip if you haven't already:

"pip install Pillow numpy"

## Installation

1. Clone this repository or download the script to your local machine.
2. Adjust the source_folder and duplicate_folder paths in the script to match your directory structure.

## Configuration

- source_folder: Directory containing the images to be analyzed.
- duplicate_folder: Directory where duplicates will be moved if their MSE is below the threshold.
- mse_threshold: MSE value below which two images are considered duplicates. Default is 45.

## Running the Script

Execute the script in your terminal or command prompt:

"python modified_MSE.py"

The script will process all images in the source_folder, compare them for similarity, and move the similar images to the duplicate_folder.

## Example Output

After running, you'll find images considered duplicates moved to the duplicate_folder, each renamed with its MSE value for reference. The terminal will also print comparisons being made, along with their MSE values:

|   |Image 1|&|Image 2|MSE Value|
|---|-------|-|-------|---------|
|A|![1](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepA1.jpg)|AND|![2](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepA2.jpg)| MSE Value=8.89 |
|B|![3](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepB1.jpg)|AND|![4](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepB2.jpg)| MSE Value=103.7|
|C|![5](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepC1.jpg)|AND|![6](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepC2.jpg)| MSE Value=12.42|
|D|![7](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepD1.jpg)|AND|![8](https://github.com/Sami3610/BioVison/blob/main/Filters/Images/RepD2.jpg)| MSE Value=93.25|


## Contributing

Contributions to improve the MSE Image Filter are welcome. Feel free to fork the repository, make your changes, and submit a pull request.

## License

This script is released under the MIT License. See the LICENSE file in the repository for more details.

## Acknowledgments

- This script was inspired by the need for an efficient way to clean up large image datasets.
- Thanks to the Python community for the invaluable libraries.
