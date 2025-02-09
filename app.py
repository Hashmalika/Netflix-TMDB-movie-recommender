import streamlit as st
import pickle
import requests
import os
import certifi

# Load the movie data and similarity index
movies = pickle.load(open("newmovielist.pkl", "rb"))
similarity = pickle.load(open("thesimilaritylist.pkl", "rb"))
movies_list = movies['title'].values

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")
st.markdown("Find your next favorite movie based on what you love!")

select_value = st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_list = []
    for i in distance[1:6]:  # If distance[0] is the movie you are trying to find recommendations for, then using distance[0:5] might include the same movie in the recommendations, which is often undesirable.
        movies_id = movies.iloc[i[0]].id
        recommend_list.append(movies.iloc[i[0]].title)
    return recommend_list

# Display recommendations
if st.button("🎥 Show Recommendations"):
    movie_name = recommend(select_value)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(f"{1}. {movie_name[0]}")
    
    with col2:
        st.text(f"{2}. {movie_name[1]}")
    
    with col3:
        st.text(f"{3}. {movie_name[2]}")
    
    with col4:
        st.text(f"{4}. {movie_name[3]}")
    
    with col5:
        st.text(f"{5}. {movie_name[4]}")
