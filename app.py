import os
from ultralytics import YOLO
import json

# Load the YOLOv8 model once to avoid reloading it on each function call
# model = YOLO("E:\\Projects_working\\Yolov8_object_detection\\model\\yolov8x.pt")

# Load the Custom fine tunned model
model = YOLO("E:\\Projects_working\\Yolov8_object_detection\\model\\yolov8_custom_detection\\weights\\best.pt")



def run_model(image, save_to_json=False, json_filename="output/results.json"):
    # Perform inference
    results = model(image)
    # print("results ", results)
    if save_to_json:
        # Prepare data to be saved in JSON format
        new_results = []
        for result in results:
            for box in result.boxes:
                print("box ", box)
                new_results.append({
                    "class": model.names[int(box.cls)],
                    "confidence": box.conf.item(),
                    "box": box.xyxy.tolist()  # Bounding box coordinates
                })

        # Check if the JSON file already exists
        if os.path.exists(json_filename):
            # Load existing data
            with open(json_filename, 'r') as json_file:
                existing_data = json.load(json_file)
        else:
            existing_data = []

        # Append new results to existing data
        existing_data.extend(new_results)

        # Save all results to the JSON file
        with open(json_filename, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)

    return results
