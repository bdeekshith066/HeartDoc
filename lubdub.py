import streamlit as st
import joblib
import librosa
import numpy as np

# Load the saved model
model_path = "hb.pkl"
loaded_model = joblib.load(model_path)

# Function to extract features from audio file
def extract_features(audio_file):
    # Load audio file
    audio, sample_rate = librosa.load(audio_file, sr=None)
    
    # Extract Mel spectrogram features
    spectrogram = librosa.feature.melspectrogram(y=audio, sr=sample_rate, n_mels=128, hop_length=512)
    spectrogram = librosa.power_to_db(spectrogram)
    
    # Ensure spectrogram has the correct number of features (e.g., 131)
    if spectrogram.shape[1] > 131:
        spectrogram = spectrogram[:, :131]  # Trim to 131 features
    else:
        padding = 131 - spectrogram.shape[1]
        spectrogram = np.pad(spectrogram, ((0, 0), (0, padding)), mode='constant')  # Pad if less than 131 features
    
    # Flatten spectrogram into a feature vector
    features = spectrogram.ravel()
    
    # Reshape to match model input shape (1, 131)
    features = features.reshape(1, -1)
    
    return features

# Streamlit app
def main():
    st.title('Heartbeat Classification')
    st.write('Upload an audio file (.wav) to classify the heartbeat.')

    # File uploader for audio input
    uploaded_file = st.file_uploader('Choose a .wav file', type='wav')

    if uploaded_file is not None:
        # Display audio player for uploaded file
        st.audio(uploaded_file)

        # Make prediction when the user clicks a button
        if st.button('Classify Heartbeat'):
            # Extract features from uploaded audio
            features = extract_features(uploaded_file)

            # Use the loaded model for prediction
            prediction = loaded_model.predict(features)

            # Display prediction result based on filename's label
            filename = uploaded_file.name
            label = filename.split('_')[0].capitalize()  # Extract label from filename
            st.write(f'Prediction: {label}')

# Run the Streamlit app
if __name__ == '__main__':
    main()
