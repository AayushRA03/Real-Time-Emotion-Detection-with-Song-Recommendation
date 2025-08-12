import cv2
import os
import random
import webbrowser
import streamlit as st
from deepface import DeepFace
import numpy as np
from PIL import Image

# Emotion-to-song mapping (Added Fear Songs)
emotion_songs = {
    "happy": {
        "Pharrell - Happy": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "Justin Timberlake - Can't Stop the Feeling": "https://www.youtube.com/watch?v=fLexgOxsZu0"
    },
    "sad": {
        "Guns N' Roses - November Rain": "https://www.youtube.com/watch?v=8SbUC-UaAxE",
        "Wiz Khalifa - See You Again": "https://www.youtube.com/watch?v=RgKAFK5djSk"
    },
    "angry": {
        "Disturbed - Down With The Sickness": "https://www.youtube.com/watch?v=04F4xlWSFh0",
        "Slipknot - Duality": "https://www.youtube.com/watch?v=soZ5ZvM-62g"
    },
    "neutral": {
        "Coldplay - The Scientist": "https://www.youtube.com/watch?v=3JZ4pnNtyxQ",
        "Ed Sheeran - Shape of You": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
    },
    "surprise": {
        "Queen - Bohemian Rhapsody": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ",
        "Imagine Dragons - Thunder": "https://www.youtube.com/watch?v=fKopy74weus"
    },
    "fear": {  # 🎃 Added Fear Emotion Songs
        "Michael Jackson - Thriller": "https://www.youtube.com/watch?v=sOnqjkJTMaA",
        "Evanescence - Bring Me to Life": "https://www.youtube.com/watch?v=3YxaaGgTQYM"
    }
}

# Streamlit UI
st.set_page_config(page_title="Emotion-Based Song Recommender", layout="centered")
st.title("🎭 Emotion-Based Song Recommender 🎵")
st.write("Click **'Capture Image'** to analyze your emotion and get a song recommendation!")

# Webcam capture
img_file_buffer = st.camera_input("Take a Picture")

# Process Image if Captured
if img_file_buffer:
    # Convert image to OpenCV format
    img = Image.open(img_file_buffer)
    img = np.array(img)

    # Save Image Temporarily
    img_path = "captured_image.jpg"
    cv2.imwrite(img_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

    # Emotion Detection
    try:
        st.write("Analyzing Emotion... Please wait.")
        analysis = DeepFace.analyze(img_path, actions=['emotion'])
        detected_emotion = analysis[0]['dominant_emotion'].capitalize()
        st.success(f"Detected Emotion: **{detected_emotion}**")

        # Get a random song based on emotion
        if detected_emotion.lower() in emotion_songs:
            song_name, song_link = random.choice(list(emotion_songs[detected_emotion.lower()].items()))
            st.subheader(f"🎶 Recommended Song: {song_name}")
            
            # Play Song Button
            if st.button("🎵 Play Song on YouTube"):
                webbrowser.open(song_link)

        else:
            st.error("No matching song found!")

    except Exception as e:
        st.error("Error in detecting emotion. Try again.")
        st.text(e)

    # Clean up saved image
    os.remove(img_path)
#streamlit run "C:\Users\Aayush Rathore\Desktop\project\songRecEmo\songreco.py"
