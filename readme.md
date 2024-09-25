# YOLOv8 Object Detection

This project is an object detection system built using the YOLOv8 model, Streamlit for the UI, and essential libraries like NumPy and PIL. It allows users to upload images, detect objects in real-time, and provides an option to save the results in JSON format.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Workflow](#workflow)
- [How to Set Up the Project](#how-to-set-up-the-project)
- [How to Run the Project](#how-to-run-the-project)
- [Fine-Tuning the Model](#fine-tuning-the-model)

## Introduction

This project is designed to showcase the capabilities of the YOLOv8 model for object detection. Users can upload an image, detect objects with real-time annotations, and optionally save the detection results as a JSON file. It is perfect for projects that require fast and accurate object detection.

## Features

- **Custom YOLOv8 Fine-Tuned Model:** Detects objects with high accuracy on custom datasets.
- **Streamlit Integration:** A responsive and user-friendly interface for uploading images and displaying detection results.
- **Real-time Object Detection:** Provides annotated images with detected objects and confidence scores.
- **JSON Output Option:** Save the detection results in a structured format for further analysis.

## Technologies Used

- **YOLOv8:** A cutting-edge object detection model known for its balance between speed and accuracy. Fine-tuned on custom datasets to improve detection of specific object classes.
- **Streamlit:** A simple framework for creating interactive web applications, used to build the front-end for uploading images and displaying the detection results.
- **NumPy:** Utilized for efficient handling and manipulation of image data during model inference.
- **Pillow (PIL):** A Python Imaging Library that handles image file formats, allowing for easy manipulation and display within the Streamlit app.

## Project Structure


├── app.py                           # main code file
├── streamlit.py                     # streamlit UI file
├── model/                           # Model folder
│   └── yolov8x.pt                   # YOLOv8 pre-trained and fine-tuned model file
├── output/                          # output folder to save JSON response
│   └── results.json                 # JSON file to store object detection results
├── fine_tuning_Data/                # Data folder (for datasets and input images)
├── finetuning.py                    # Script for fine-tuning the YOLOv8 model on custom datasets
├── requirements.txt                 # Python dependencies
└── README.md                        # This README file


## Workflow

- User Interaction: Users upload an image using the Streamlit web application.
- Object Detection: The YOLOv8 model detects objects in the uploaded image, annotating them with bounding boxes and confidence scores.
- Result Display: Both the original and annotated images are displayed side by side in the Streamlit app for comparison.
- JSON Output: Optionally, users can save the object detection results as a JSON file, containing class names, confidence scores, and bounding box coordinates.

## How to Set Up the Project

Clone the repository:

bash
git clone https://github.com/your-username/YOLOv8_Object_Detection.git
cd YOLOv8_Object_Detection

### Install dependencies: Ensure you have Python 3.9.x installed, then run:

bash
pip install -r requirements.txt

### Prepare the dataset (if fine-tuning the model): Organize your dataset and update the paths in data.yaml.

- How to Run the Project
- Run the Streamlit application:

bash
streamlit run streamlit.py

### Upload an image and start detecting objects: Use the user-friendly interface to upload an image and see the detection results.

## Fine-Tuning the Model

- Prepare the dataset: Create or label your dataset using a tool like Roboflow, then modify the data.yaml file with your dataset path and class labels.

- Run Fine-Tuning: Modify the finetuning.py script to point to your dataset and desired output location for the fine-tuned model, then run:

bash
python finetuning.py

