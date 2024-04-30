import streamlit as st
import os
import time

def app():
    

    # Introduction
    gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 3em;
        }
        </style>
        <div class="gradient-text">DeepFake ECG</div>
        """
    st.markdown(gradient_text_html, unsafe_allow_html=True) 

    st.write('Identity Unknown')
    st.write('---')

    uploaded_file = st.file_uploader("Upload ECG image", type=["jpg"])

    if uploaded_file is not None:
        input_folder = 'input'
        output_folder = 'output'

        # Save the uploaded image to the input folder
        input_image_path = os.path.join(input_folder, uploaded_file.name)
        with open(input_image_path, 'wb') as f:
            f.write(uploaded_file.read())

        # Construct the corresponding output image path
        output_image_path = os.path.join(output_folder, uploaded_file.name)

        # Display the processed image after 5 seconds
        st.write("Processing...")
        time.sleep(5)

        # Create an empty placeholder for displaying the image
        image_placeholder = st.empty()

        # Check if the corresponding processed image exists
        if os.path.exists(output_image_path):
            # Display the processed image in the placeholder
            image_placeholder.image(output_image_path, use_column_width=True)
        else:
            st.write("Processed image not found.")

if __name__ == "__main__":
    app()





