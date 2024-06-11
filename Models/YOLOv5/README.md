# Introduction

YOLOv5 is one of the latest iterations in the series of YOLO (You Only Look Once) models, a family of object detection architectures that have gained widespread popularity for their speed and accuracy. Developed and maintained by [Ultralytics](https://github.com/ultralytics/yolov5), YOLOv5 represents a significant advancement in real-time object detection, making it a good choice for applications in a variety of fields from urban vegetation surveillance to autonomous driving. The flexibility of YOLOv5 allows it to be customized through different training techniques, accommodating specific project needs and enhancing model performance across varied datasets.

- Basic Training: this approach refers to the process of training the YOLOv5 model from scratch. This approach is ideal for big datasets that are significantly different from common datasets like COCO or PASCAL VOC, on which many pre-trained models are based. Training from scratch involves initializing the model's weights randomly and adjusting them through a full training cycle. Although computationally intensive, this allows for custom learning on unique data, tailoring the model precisely to specific needs.

- Transfer Learning: it is a powerful strategy in machine learning where a model developed for one task is repurposed as the starting point for another related task. For YOLOv5, this means initiating the training process with a model pre-trained on a comprehensive and diverse dataset such as COCO. This approach is particularly advantageous when dealing with limited data or when the new task bears similarities to the original training context. It significantly reduces training time and often enhances model performance, enabling the model to leverage learned features that generalize well across similar tasks.

- Freezing Layers: this technique is used to pinpoint model adaptation by preventing updates to certain parts of the network during backpropagation. This method comes in two forms:

** Freezing Backbone Layers: Typically, only the early layers of the model are frozen. These layers, responsible for capturing basic visual features like edges and textures, are usually well-generalized across different types of images and do not require retraining.
** Freezing All Layers: This approach involves freezing almost the entire network except for the final layers. It is useful when adapting the model to new, but closely related tasks where high-level features learned from the original dataset are still applicable.

## Installation and Usage

This section details the steps required to set up your environment and start training the YOLOv5 models using various configurations and customizations.

# Initial Setup

1. Install the Ultralytics YOLOv5 repository:

Begin by installing the Ultralytics package directly via pip, which is useful for other Ultralytics utilities, followed by cloning the YOLOv5 repository and installing its dependencies:

pip install ultralytics  # Install Ultralytics package
git clone https://github.com/ultralytics/yolov5  # Clone YOLOv5 repository
cd yolov5
pip install -r requirements.txt  # Install dependencies

* Basic Training Configuration

For basic training, you will run the YOLOv5 training script with the following parameters, which can be adjusted based on your specific requirements:

"python train.py --data coco.yaml --epochs 300 --weights yolov5s.pt --cfg yolov5n.yaml --batch-size 128
"

- Weights: Choose from [yolov5n.pt, yolov5s.pt, yolov5m.pt, yolov5l.pt, yolov5x.pt] depending on the size and capacity of the model you intend to train.

- Configuration File (--cfg): Corresponding to the chosen weights, use one of [yolov5n, yolov5s, yolov5m, yolov5l, yolov5x].

- Batch Size: Can be [16, 32, 64, 128] depending on your GPU memory.

* Transfer Learning Configuration

For transfer learning, specify the path to your pre-trained model in the weights argument:

"python train.py --data coco.yaml --epochs 100 --weights path/to/your/pretrained_model.pt --cfg yolov5s.yaml --batch-size 32"

Replace path/to/your/pretrained_model.pt with the actual file path of your pre-trained model.

* Freezing Layers
When you need to freeze layers during training:

** Freezing Backbone Layers:

"python train.py --data coco.yaml --epochs 100 --weights yolov5s.pt --cfg yolov5s.yaml --batch-size 32 --freeze 10"

** Freezing All Layers:

"python train.py --data coco.yaml --epochs 100 --weights yolov5s.pt --cfg yolov5s.yaml --batch-size 32 --freeze 24"

Adjust the --freeze value based on the number of layers you wish to freeze. For example, --freeze 10 for freezing early layers and --freeze 24 to almost freeze all layers, depending on the model architecture.

## Running the Models

After setting up your model configuration as described above, run the training command tailored to your chosen approach. Monitor the output to ensure the training is progressing as expected.

## Model Validation

After training your models, it's crucial to assess their performance to ensure they meet your project's accuracy and efficiency standards. The validation step uses a separate set of data to evaluate the model and is executed with the following command:

"python val.py --weights 'path/to/trained-model.pt' --data /path/to/data.yaml --img 640"

* Validation Parameters Explained

- Weights: Specify the path to your trained model file. Replace 'path/to/trained-model.pt' with the actual path to the model file you wish to validate.
- Data: Point to your data configuration file. This should be the same file used during training unless otherwise specified for separate validation datasets. Replace /path/to/data.yaml with the actual path to your data configuration file.
- Image Size (--img): The size of the images for validation. Here, 640 denotes the image dimensions (640x640 pixels), which should match or be representative of the training configuration for accurate validation results.

## Interpreting Validation Results

- Precision: Measures the accuracy of positive predictions. High precision indicates that the model returns more relevant results than irrelevant.
- Recall: Measures the model's ability to find all relevant cases within a dataset. High recall means that the model returns most of the relevant results.
- mAP: A comprehensive metric that combines precision and recall. It's particularly useful when you want to balance these two metrics against each other.
Use these metrics to fine-tune your model parameters, retrain if necessary, and ensure that the model is ready for deployment or further testing.

## Using the Trained Models for Detection

After training and validating your models, the next step is to use them for object detection tasks. The YOLOv5 model provides a straightforward method to apply the trained weights to detect objects in images.

To perform detection using your trained model, use the following command structure in your terminal:

"python detect.py --source 'images_folder_location' --weights 'trained_model.pt' --save-txt"

--source: Specifies the location of the source images or video files where the model will perform detection. Replace 'images_folder_location' with the path to your data. This can be a path to a folder containing images, a single image, a video file, or even a URL to a webcam.

--weights: Indicates the path to the trained model file. Replace 'trained_model.pt' with the path to your specific trained model file.

--save-txt: When included, this flag directs the script to save bounding box coordinates in a text file for each input image, which is useful for further analysis or processing.

For detailed results and trained models, please refer to the [Trained Models] (./YOLOv5/Trained Models) folder containing trained models and outputs.










