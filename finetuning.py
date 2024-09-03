import os
from ultralytics import YOLO

# Specify the path to your data.yaml file
data_yaml = "fine_tuning_Data/data.yaml"

# Load the pre-trained YOLOv8 model
model = YOLO("E:\\Projects_working\\Yolov8_object_detection\\model\\yolov8x.pt")

# Train the model and specify the project directory
model.train(
    data=data_yaml,
    epochs=10,
    batch=1,
    imgsz=640,
    name="yolov8_custom_detection",
    project="E:\\Projects_working\\Yolov8_object_detection\\model",  # Specify the project directory
    device="cpu"
)

# Optionally, evaluate the model
# metrics = model.val()

# Save the trained model (if you want to rename or save separately)
# model.save("E:\\Projects_working\\Yolov8_object_detection\\model\\yolov8_fish_detection.pt")
