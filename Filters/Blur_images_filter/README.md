# Blur Images Filters

Blur in digital images is a common yet complex issue, often introduced by environmental factors or camera movement. This challenge is especially prevalent in fields requiring precise image analysis, such as remote sensing, astronomy, microscopy, and medical imaging. Blurry images, resulting primarily from dynamic lens movement during capture, significantly hinder the ability to accurately interpret and analyze data. In urban continuous imaging scenarios—where an imaging system is mounted on a moving vehicle—camera instability due to road conditions like potholes, speed bumps, and uneven surfaces exacerbates the problem, producing images that lack the clarity needed for thorough analysis.

To combat this issue and ensure the integrity of image datasets, two sophisticated blur detection and removal techniques have been developed and tested within this repository: the Fast Fourier Transform (FFT) technique and the Laplacian Variance technique. These methods are designed to identify and filter out blurred images from datasets, retaining only those images that meet the requisite quality standards for precise and reliable study findings.

## Overview of Techniques

- Fast Fourier Transform (FFT) Technique: This technique transforms an image from its spatial domain to the frequency domain, enabling the identification of blurred images through the analysis of frequency components. Blurred images exhibit a lack of high-frequency components, which are indicative of sharp edges and details. The FFT technique efficiently discriminates between clear and blurred images based on their frequency spectra.

- Laplacian Variance Technique: By applying the Laplacian operator—a second-order derivative method that highlights areas of rapid intensity change indicative of edges—this technique calculates the variance of the Laplacian to assess image quality in terms of blur. Images with low Laplacian variance are classified as blurred and are thus filtered out from the dataset.

## Directory Structure

This repository is organized into two main subfolders, each dedicated to one of the blur detection techniques:

* FFT: Contains the script and documentation for the FFT-based blur detection method.

* laplacian_variance: Houses the script and README for the Laplacian Variance-based blur detection approach.

## Getting Started

To utilize these filters, navigate to the respective subfolder for detailed instructions on installation, configuration, and execution. Each subfolder's README file provides comprehensive guidance on deploying the corresponding technique to identify and remove blurred images from your dataset.

## Contributing

Contributions to enhance the blur detection capabilities of this repository are welcome. Whether it's refining existing techniques or introducing new methods, please feel free to fork the repository, implement your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

Appreciation to the researchers and developers in the fields of digital image processing and computer vision, whose foundational work underpins the techniques employed in this repository.