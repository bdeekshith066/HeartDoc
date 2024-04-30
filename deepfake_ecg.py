import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def process_image(image):
    # Example image processing function (replace with your own processing logic)
    # Convert PIL image to numpy array for processing
    img_array = np.array(image)

    # Perform image processing (e.g., generate a modified image)
    processed_image = img_array  # Placeholder for actual image processing

    return processed_image

def main():
    st.title('Image Processing with Streamlit')

    # File uploader for image input
    uploaded_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption='Original Image', use_column_width=True)

        # Process the uploaded image
        processed_image = process_image(original_image)

        # Display the processed image
        st.subheader('Processed Image')
        st.image(processed_image, caption='Processed Image', use_column_width=True)

if __name__ == '__main__':
    main()
