import pickle
import streamlit as st
import requests

# -----------------------------
# TMDB Poster Fetcher
# -----------------------------
API_KEY = "7fbd0c04887929e22abf085398a5e167"

def fetch_poster(content_id, content_type):
    if content_type == "Movie":
        url = f"https://api.themoviedb.org/3/movie/{content_id}?api_key={API_KEY}&language=en-US"
    else:
        url = f"https://api.themoviedb.org/3/tv/{content_id}?api_key={API_KEY}&language=en-US"

    data = requests.get(url).json()
    poster_path = data['poster_path']

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None


# -----------------------------
# Generic Recommendation Logic
# -----------------------------
def recommend(title, data, similarity, content_type, n=10):
    index = data[data['title'] == title].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    names = []
    posters = []

    for i in distances[1:n+1]:
        content_id = data.iloc[i[0]].id
        names.append(data.iloc[i[0]].title)
        posters.append(fetch_poster(content_id, content_type))

    return names, posters


# -----------------------------
# Load Data
# -----------------------------
movies = pickle.load(open("movie.pkl", "rb"))
movie_similarity = pickle.load(open("movies_similarity.pkl", "rb"))

tv_shows = pickle.load(open("series.pkl", "rb"))
tv_similarity = pickle.load(open("series_similarity.pkl", "rb"))


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🎬 Movie & TV Show Recommendation System")

choice = st.selectbox(
    "What do you want recommendations for?",
    ("Movies", "TV Shows")
)

if choice == "Movies":
    selected = st.selectbox("Select a Movie", movies['title'].values)

    if st.button("Recommend Movies"):
        names, posters = recommend(
            selected, movies, movie_similarity, "Movie", n=10
        )

        cols = st.columns(5)
        for i in range(len(names)):
            with cols[i % 5]:
                st.text(names[i])
                st.image(posters[i])


else:
    selected = st.selectbox("Select a TV Show", tv_shows['title'].values)

    if st.button("Recommend TV Shows"):
        names, posters = recommend(
            selected, tv_shows, tv_similarity, "TV", n=10
        )

        cols = st.columns(5)
        for i in range(len(names)):
            with cols[i % 5]:
                st.text(names[i])
                st.image(posters[i])
