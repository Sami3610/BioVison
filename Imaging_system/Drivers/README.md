# Overview

These folders contain the drivers necessary to operate the imaging system, built on a Python-based framework leveraging the Robot Operating System (ROS) for efficient message passing and process management. The drivers facilitate the processing and saving of images from dual sources, using OpenCV for image manipulation and cv_bridge for conversion between ROS image messages and OpenCV formats. 

In addition to real-time image processing, these drivers maintain a link with GPS data, tagging images with geographical locations corresponding to their real-world coordinates. This setup allows for concurrent handling of two separate image streams, with images and their metadata (including GPS coordinates and timestamps) being saved to specified file paths and logged in a CSV file for subsequent analysis.

## Features

- **Image Processing**: Utilizes OpenCV to process images from two different sources.

- **Data Tagging**: Combines image data with GPS coordinates for geographical mapping.

- **File Management**: Dynamic update of file paths and meticulous logging of image metadata in a CSV file.

- **Data Integrity**: Ensures all data is properly saved before system shutdown to guarantee data integrity during field operations.

## Installation

Before running the drivers, ensure that the ROS environment is set up on your system. 

## Running the Drivers

To operate the imaging system drivers, execute the following commands in your terminal. These commands will set up the ROS environment and launch the camera control:

1. **Set Up the ROS Environment:**

 ```bash
   source ~/desktop/testcamera/devel/setup.bash
   ```
2. **Launch the Camera Control**

 ```bash
   roslaunch cameracontrol cameracontrol.launch
   ```

## Data Collection Routes

With the imaging system fully assembled, including both hardware and software configurations, the focus now shifts to the practical application. The next steps involve selecting specific routes for data collection tailored to target specific tree species. This approach not only navigates through urban spaces but also considers factors such as tree distribution, species prevalence, and accessibility. The methodology for designing these routes is discussed in a subsequent subsection.

## Further Documentation

Refer to the additional documentation provided in the corresponding [hardware folder](https://github.com/Sami3610/BioVison/blob/main/Imaging_system/Hardware/README.md) for more details on the physical components of the imaging system.




