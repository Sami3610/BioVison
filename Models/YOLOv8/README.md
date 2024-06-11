# # Introduction

YOLOv8, published in 2023, is the latest iteration in the YOLO (You Only Look Once) family of object detection models, renowned for their speed and accuracy. Developed and maintained by [Ultralytics](https://github.com/ultralytics/yolov8), YOLOv8 introduces significant advancements in real-time object detection. Its architecture enhances detection performance, making it highly suitable for a variety of applications, including automated surveillance, wildlife monitoring, autonomous driving, and industrial automation. The flexibility of YOLOv8 allows for customization through different training techniques, enabling it to meet specific project needs and improve model performance across diverse datasets.

- **Basic Training**: This method involves training the YOLOv8 model from the ground up using a new dataset. It is particularly beneficial for large datasets that differ significantly from widely used datasets like COCO or PASCAL VOC. Training from scratch entails initializing the model's weights randomly and then refining them through an entire training cycle. While this process is computationally demanding, it enables the model to learn directly from unique data, thereby tailoring the model precisely to the specific requirements of the new dataset

- **Transfer Learning**: This is a highly effective machine learning technique where a model developed for one task is adapted for a different but related task. In the context of YOLOv8, transfer learning involves starting the training process with a model that has already been pre-trained on a broad and diverse dataset like COCO. This strategy is especially useful when working with limited data or when the new task is closely related to the original one. It greatly reduces training time and often improves model performance by utilizing pre-learned features that generalize well to similar tasks.

## Installation and Usage

This section details the steps required to set up your environment and start training the YOLOv8 models using various configurations and customizations.

### Initial Setup

1. Install the Ultralytics YOLOv8 repository:

Begin by installing the Ultralytics package directly via pip, which is useful for other Ultralytics utilities, followed by cloning the YOLOv8 repository and installing its dependencies:

```bash
pip install ultralytics  # Install Ultralytics package
git clone https://github.com/ultralytics/yolov8  # Clone YOLOv8 repository
cd yolov8
pip install -r requirements.txt  # Install dependencies
```
## Basic Training Configuration

For basic training, you will run the YOLOv8 training script with the following parameters, which can be adjusted based on your specific requirements:

```bash
python train.py --data coco.yaml --epochs 300 --weights yolov8s.pt --cfg yolov8n.yaml --batch-size 128
```
- Weights: Choose from [yolov8n.pt, yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt] depending on the size and capacity of the model you intend to train.
- Configuration File (--cfg): Corresponding to the chosen weights, use one of [yolov8n, yolov8s, yolov8m, yolov8l, yolov8x].
- Batch Size: Can be [16, 32, 64, 128] depending on your GPU memory.

## Transfer Learning Configuration

For transfer learning, specify the path to your pre-trained model in the weights argument:

```bash
python train.py --data coco.yaml --epochs 100 --weights path/to/your/pretrained_model.pt --cfg yolov8s.yaml --batch-size 32
```
Replace path/to/your/pretrained_model.pt with the actual file path of your pre-trained model.

## Running the Models

After setting up your model configuration as described above, run the training command tailored to your chosen approach. Monitor the output to ensure the training is progressing as expected.

## Model Validation

After training your models, it's crucial to assess their performance to ensure they meet your project's accuracy and efficiency standards. The validation step uses a separate set of data to evaluate the model and is executed with the following command:

```bash
python val.py --weights 'path/to/trained-model.pt' --data /path/to/data.yaml --img 640
```

## Validation Parameters Explained

- Weights: Specify the path to your trained model file. Replace 'path/to/trained-model.pt' with the actual path to the model file you wish to validate.
- Data: Point to your data configuration file. This should be the same file used during training unless otherwise specified for separate validation datasets. Replace /path/to/data.yaml with the actual path to your data configuration file.
- Image Size (--img): The size of the images for validation. Here, 640 denotes the image dimensions (640x640 pixels), which should match or be representative of the training configuration for accurate validation results.

## Interpreting Validation Results

- Precision: Measures the accuracy of positive predictions. High precision indicates that the model returns more relevant results than irrelevant.
- Recall: Measures the model's ability to find all relevant cases within a dataset. High recall means that the model returns most of the relevant results.
- mAP: A comprehensive metric that combines precision and recall. It's particularly useful when you want to balance these two metrics against each other.

Use these metrics to fine-tune your model parameters, retrain if necessary, and ensure that the model is ready for deployment or further testing.

## Using the Trained Models for Detection

After training and validating your models, the next step is to use them for object detection tasks. The YOLOv8 model provides a straightforward method to apply the trained weights to detect objects in images.

To perform detection using your trained model, use the following command structure in your terminal:

```bash
python detect.py --source 'images_folder_location' --weights 'trained_model.pt' --save-txt
```
- Source: Specifies the location of the source images or video files where the model will perform detection. Replace 'images_folder_location' with the path to your data. This can be a path to a folder containing images, a single image, a video file, or even a URL to a webcam.
- Weights: Indicates the path to the trained model file. Replace 'trained_model.pt' with the path to your specific trained model file.
- Save-txt: When included, this flag directs the script to save bounding box coordinates in a text file for each input image, which is useful for further analysis or processing.

For detailed results and trained models, please refer to the [Trained Models] (./YOLOv8/Trained Models) folder containing trained models and outputs.

