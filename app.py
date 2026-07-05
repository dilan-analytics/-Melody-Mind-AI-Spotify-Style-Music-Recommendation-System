import streamlit as st
import pandas as pd
import numpy as np
import urllib.parse

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="MelodyMind AI",
    page_icon="🎧",
    layout="wide"
)

# -----------------------------
# 🎨 BEAUTIFUL UI (CSS + ANIMATIONS)
# -----------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(120deg, #121212, #1a1a1a);
    color: white;
}

/* Animated Title */
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #1DB954;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% {transform: scale(1);}
    50% {transform: scale(1.03);}
    100% {transform: scale(1);}
}

/* Song Card */
.card {
    background-color: #181818;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    border-left: 4px solid #1DB954;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.02);
    background-color: #202020;
}

/* Buttons */
.stButton > button {
    background-color: #1DB954;
    color: black;
    font-weight: bold;
    border-radius: 8px;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #1ed760;
    transform: scale(1.05);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0e0e0e;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("spotify_with_mood.csv")

# -----------------------------
# FEATURES
# -----------------------------
features = [
    'danceability',
    'energy',
    'loudness',
    'speechiness',
    'acousticness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo'
]

X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

knn = NearestNeighbors(n_neighbors=11, metric='cosine')
knn.fit(X_scaled)

# -----------------------------
# FAVORITES SYSTEM
# -----------------------------
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# -----------------------------
# SIDEBAR MENU
# -----------------------------
menu = st.sidebar.selectbox(
    "🎧 Navigation",
    ["🏠 Home", "🎵 Song Match", "😊 Mood", "🎼 Genre", "🔥 Trending", "❤️ Favorites"]
)

# -----------------------------
# HOME
# -----------------------------
if menu == "🏠 Home":

    st.markdown('<div class="title">🎧 MelodyMind AI</div>', unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1511379938547-c1f69419868d",
        use_container_width=True
    )

    st.success("✨ AI Powered Music Recommendation System using Machine Learning")

# -----------------------------
# SONG RECOMMENDATION
# -----------------------------
elif menu == "🎵 Song Match":

    st.markdown('<div class="title">🎵 Find Similar Songs</div>', unsafe_allow_html=True)

    song_name = st.selectbox("Search Song", df['track_name'].sort_values().unique())

    def recommend(song_name):

        idx = df[df['track_name'] == song_name].index[0]

        distances, indices = knn.kneighbors(X_scaled[idx].reshape(1, -1))

        st.subheader("🎧 Recommended Songs")

        for i in range(1, len(indices[0])):

            song_idx = indices[0][i]

            song_title = df.iloc[song_idx]['track_name']
            artist = df.iloc[song_idx]['artists']

            query = song_title + " " + artist
            url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)

            col1, col2 = st.columns([4, 1])

            with col1:
                st.markdown(f"""
                <div class="card">
                    🎵 <b>{song_title}</b><br>
                    👤 {artist}
                </div>
                """, unsafe_allow_html=True)

                if st.button(f"❤️ Like", key=song_idx):
                    st.session_state.favorites.append(song_title)
                    st.success("Added to favorites!")

                st.link_button("▶ Play Preview", url)

            with col2:
                st.metric("Match", f"{1 - distances[0][i]:.2f}")

    if st.button("Generate Recommendations"):
        recommend(song_name)

# -----------------------------
# MOOD
# -----------------------------
elif menu == "😊 Mood":

    st.markdown('<div class="title">😊 Music by Mood</div>', unsafe_allow_html=True)

    mood = st.selectbox("Choose Mood", df['mood'].unique())

    if st.button("Get Songs"):

        songs = df[df['mood'] == mood].sort_values(by="popularity", ascending=False)

        for i in range(min(10, len(songs))):

            song_title = songs.iloc[i]['track_name']
            artist = songs.iloc[i]['artists']

            col1, col2 = st.columns([4, 1])

            with col1:
                st.markdown(f"""
                <div class="card">
                    🎶 <b>{song_title}</b><br>
                    👤 {artist}
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.metric("Popularity", songs.iloc[i]['popularity'])

# -----------------------------
# GENRE
# -----------------------------
elif menu == "🎼 Genre":

    st.markdown('<div class="title">🎼 Genre Explorer</div>', unsafe_allow_html=True)

    genre = st.text_input("Enter Genre")

    if st.button("Search"):

        songs = df[df['track_genre'] == genre].sort_values(by="popularity", ascending=False)

        for i in range(min(10, len(songs))):

            col1, col2 = st.columns([4, 1])

            with col1:
                st.markdown(f"""
                <div class="card">
                    🎵 <b>{songs.iloc[i]['track_name']}</b><br>
                    👤 {songs.iloc[i]['artists']}
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.metric("Popularity", songs.iloc[i]['popularity'])

# -----------------------------
# TRENDING
# -----------------------------
elif menu == "🔥 Trending":

    st.markdown('<div class="title">🔥 Trending Songs</div>', unsafe_allow_html=True)

    trending = df.sort_values(by="popularity", ascending=False).head(10)

    for i in range(10):

        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(f"""
            <div class="card">
                🔥 <b>{trending.iloc[i]['track_name']}</b><br>
                👤 {trending.iloc[i]['artists']}
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.metric("Popularity", trending.iloc[i]['popularity'])

# -----------------------------
# FAVORITES
# -----------------------------
elif menu == "❤️ Favorites":

    st.markdown('<div class="title">❤️ Your Favorites</div>', unsafe_allow_html=True)

    if len(st.session_state.favorites) == 0:
        st.info("No favorites yet!")
    else:
        for song in st.session_state.favorites:
            st.markdown(f"""
            <div class="card">
                ❤️ {song}
            </div>
            """, unsafe_allow_html=True)