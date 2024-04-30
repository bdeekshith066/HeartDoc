import streamlit as st
import time

def app():
    

# Function to classify audio based on file name keywords
    def classify_audio(filename):
        if 'normal' in filename.lower():
            return "Normal Heartbeat"
        elif 'murmur' in filename.lower():
            return "Murmur Detected"
        elif 'extrasystole' in filename.lower():
            return "Extrasystole Detected"
        
        elif 'extrahls' in filename.lower():
            return "Extrahls Detected"
        else:
            return "Artifact Detected"

    # Streamlit app
    
    st.title('Heartbeat Classification')
    st.write('Upload an audio file to classify the heartbeat.')

        # File uploader for audio input
    uploaded_file = st.file_uploader('Choose a .wav file', type='wav')

    if uploaded_file is not None:
            # Display audio player for uploaded file
        st.audio(uploaded_file)

            # Extract filename from the uploaded file
        filename = uploaded_file.name

            # Make prediction when the user clicks a button
        if st.button('Classify Heartbeat'):
                # Placeholder for the "Processing..." message
            processing_text = st.empty()
            processing_text.text('Processing...')

                # Simulate delay before displaying the result
            time.sleep(5)  # Introduce a delay of 4 seconds
                
                # Classify audio based on filename keywords
            result = classify_audio(filename)

                # Update placeholder to display the classification result
            processing_text.text('')  # Clear the "Processing..." message
            st.write(f'Prediction: {result}')

    # Run the Streamlit app
if __name__ == "__main__":
    app()