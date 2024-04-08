# Similar Images Filters

In the context of urban imaging projects, particularly those involving continuous imaging via vehicles, one notable challenge is the prevalence of repetitive images. These redundancies make the dataset bigger and increase the time needed for analysis. The root cause of such repetitions often traces back to the inevitable pauses in vehicle movement—be it due to traffic signals, adherence to traffic regulations, or the manual activation of the imaging system post-setup. Consequently, the imaging system, once activated, captures a series of near-identical images until the vehicle resumes motion, generating superfluous data that demands extensive processing time.

Recognizing the crucial need to streamline data analysis by eliminating redundant images, this folder introduces two distinct methods designed to identify and remove such similarities from imaging datasets. Each method is contained within its own subfolder, providing tailored solutions to address this widespread issue.

- Mean Square Error (MSE) Technique: Located in the similarity.detection_MSE subfolder, this method quantitatively assesses the error or similarity between pairs of images through pixel value comparisons. Images with MSE below a predetermined threshold are deemed duplicates and are efficiently segregated, thus enhancing the dataset's overall quality.

- Normalized Cross-Correlation (NCC) Technique: Found in the similarity.detection_NCC subfolder, this approach leverages statistical correlation to measure the similarity between two images. By identifying pairs with NCC values surpassing a set threshold, the script flags and relocates near-identical images, significantly reducing dataset redundancy.

The primary objective of deploying these filters is to reduce the analysis time by purging repetitive images, thereby optimizing the efficiency of urban imaging projects. Each technique has been meticulously tested and evaluated for effectiveness in addressing the specific challenges posed by the imaging system's operational nuances, including those induced by vehicular stops and the manual activation of the system.

## Getting Started

To apply these filters to your dataset, refer to the README files within each subfolder for detailed instructions on installation, configuration, and execution.

## Contributing

We welcome contributions, enhancements, and bug fixes from the community. Please refer to each subfolder's contributing guidelines for more information on how you can participate in the development and improvement of these techniques.

## Acknowledgments

Our gratitude extends to all contributors and researchers whose insights and efforts have been instrumental in the development of these image filtering solutions. Special thanks to the Python community for their invaluable libraries and support.