
# 🎭 Real-Time Emotion Detection with Song Recommendation 🎵

A real-time web app built with **Streamlit** and **DeepFace** that detects your emotion from a captured image and recommends a song that matches your mood.

---

## 📌 Features

* **Real-Time Emotion Detection** using your webcam.
* **Automatic Song Recommendation** based on detected emotion.
* **Interactive UI** with one-click song playback on YouTube.
* Supports multiple emotions: `Happy`, `Sad`, `Angry`, `Neutral`, `Surprise`, `Fear`.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (UI & Web App)
* **DeepFace** (Emotion Recognition)
* **OpenCV** (Image Processing)
* **Pillow (PIL)** (Image Handling)
* **NumPy** (Array Processing)
* **Webbrowser** (Song Playback)

---

## 📂 Project Structure

```
📁 songRecEmo/
│── songreco.py      # Main application code
│── requirements.txt # Dependencies
│── README.md        # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/Real-Time-Emotion-Detection-Song-Recommendation.git
cd Real-Time-Emotion-Detection-Song-Recommendation
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
streamlit
opencv-python
deepface
pillow
numpy
```

### 3️⃣ Run the App

```bash
streamlit run songreco.py
```

---

## 🎯 How It Works

1. Click **"Take a Picture"** using your webcam.
2. The app analyzes your image with **DeepFace** to detect your dominant emotion.
3. A random song from the matching emotion category is recommended.
4. Click **"Play Song on YouTube"** to enjoy your music.

---

## 🎭 Supported Emotions & Example Songs

| Emotion  | Example Song 1         | Example Song 2                             |
| -------- | ---------------------- | ------------------------------------------ |
| Happy    | Pharrell - Happy       | Justin Timberlake - Can't Stop the Feeling |
| Sad      | November Rain          | See You Again                              |
| Angry    | Down With The Sickness | Duality                                    |
| Neutral  | The Scientist          | Shape of You                               |
| Surprise | Bohemian Rhapsody      | Thunder                                    |
| Fear     | Thriller               | Bring Me to Life                           |

---

