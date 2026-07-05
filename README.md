# 🎵 MelodyMind AI – Spotify Style Music Recommendation System

![Banner](assets/banner.png)

---

## 🚀 Overview

**MelodyMind AI** is an AI-powered Spotify-style music recommendation system built using Machine Learning and Streamlit.

It helps users discover music based on:
- 🎧 Audio similarity (KNN model)
- 😊 Mood detection
- 🎼 Genre preferences
- 🔥 Trending popularity

This project simulates a real-world recommendation engine similar to Spotify.

---

## ✨ Key Features

### 🎵 Smart Recommendation Engine
- Find songs similar to any input track
- Uses K-Nearest Neighbors (KNN)
- Cosine similarity for better accuracy

### 😊 Mood-Based Recommendations
- Happy
- Sad
- Energetic
- Calm
- Workout
- Party

### 🎼 Genre Explorer
- Filter songs by genre
- Sort by popularity

### 🔥 Trending Songs
- Displays top popular songs

### ❤️ Favorites System
- Save liked songs during session

### 🎧 Music Preview
- Direct YouTube search links for preview

---

## 🧠 Machine Learning Approach

### Algorithms Used:
- K-Nearest Neighbors (KNN)
- Cosine Similarity
- Feature Scaling (StandardScaler)

### Why KNN?
KNN is used because it:
- Finds similar songs based on audio features
- Works well with high-dimensional data
- Simple yet powerful for recommendation systems

---

## 📊 Dataset Information

The system uses Spotify audio features:

| Feature | Description |
|--------|-------------|
| danceability | How suitable a track is for dancing |
| energy | Intensity and activity level |
| loudness | Volume of the track |
| speechiness | Presence of spoken words |
| acousticness | Acoustic nature of the song |
| instrumentalness | Presence of instruments |
| liveness | Presence of audience |
| valence | Positivity of the song |
| tempo | Speed of the song |

---

## 🏗️ System Architecture

```
Dataset → Cleaning → Feature Selection → Scaling → KNN Model → Streamlit UI → Recommendations
```

---

## 🖥️ Tech Stack

- Python 🐍
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- HTML/CSS (UI styling)

---

## 📁 Project Structure

```
MelodyMind-AI/
│
├── app.py
├── spotify_with_mood.csv
├── requirements.txt
├── README.md
│
├── assets/
│   ├── banner.png
│   ├── app_screenshot.png
```

---

## 🚀 How to Run Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run Streamlit app
```bash
streamlit run app.py
```

---

## 📸 UI Preview

> Add screenshots of your app here

- Home Page
- Recommendation Page
- Mood System
- Trending Songs

---

## 💡 Future Improvements

- 🎤 Spotify API integration (real-time songs)
- 🤖 AI chatbot music assistant
- 👤 User login system
- 📱 Mobile responsive UI
- ☁ Deploy on cloud (Streamlit / AWS)

---

## 🏆 Project Highlights

✔ Real-world ML recommendation system  
✔ Spotify-inspired UI  
✔ Multiple recommendation strategies  
✔ Clean Streamlit web app  
✔ Portfolio-ready project for internships  

---

## 👨‍💻 Author

**Dilan Karunanayake**  
AI & Data Science Enthusiast  
Machine Learning Developer  

---

## ⭐ Support

If you like this project:
⭐ Star the repository  
🚀 Share with others  
💡 Improve and contribute  
