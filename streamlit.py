import streamlit as st
from PIL import Image
import numpy as np
from app import run_model, model  # Import the run_model function and the model

# Streamlit app
st.title("YOLOv8 Object Detection")
st.write("Upload an image to detect objects using the YOLOv8 model.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# JSON file saving option
save_json = st.checkbox('Save results to JSON file')

# Submit button
submit_button = st.button('Submit')

if uploaded_file is not None and submit_button:
    # Convert the uploaded file to an OpenCV image
    image = Image.open(uploaded_file)
    image = np.array(image)
    
    # Run object detection with the option to save results to JSON
    results = run_model(image, save_to_json=save_json)

    # Annotate the image with the detected objects
    annotated_image = image.copy()
    for result in results:
        annotated_image = result.plot()  # Use the 'plot' method to render the annotations on the image

    # Create two columns for side-by-side image display
    col1, col2 = st.columns(2)

    # Display the original image in the first column
    with col1:
        st.image(image, caption='Uploaded Image', use_column_width=True)

    # Display the annotated image in the second column
    with col2:
        st.image(annotated_image, caption='Annotated Image', use_column_width=True)

    # Print the results
    st.write("Detected Objects:")
    for result in results:
        for box in result.boxes:
            cls_name = model.names[int(box.cls)]
            confidence = box.conf.item()  # Convert tensor to a float using .item()
            st.write(f"Class: {cls_name} - Confidence: {confidence:.2f}")
