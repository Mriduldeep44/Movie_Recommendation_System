import streamlit as st 
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = " https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)
    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZGJlMjFhNjlmNTM5ZWVkZDE2YjFiYjQ2NDc3OGQzNyIsIm5iZiI6MTcyOTAzMzg1Ni44Njc2MjksInN1YiI6IjY3MGVmNDk5NTQ3ZGU0YTc0ZjYwYWFiZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Cphf42qDVXZFzeZJib3NLrW1Z6PaZW61zpC19cXv9hU"
}
    data = requests.get(url,headers=headers)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

st.title("Movie recommender System")
movie_dict=pickle.load(open("movie_dict.pkl","rb"))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open("similarity.pkl","rb"))




def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movie_names=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster form the api
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movie_names,recommended_movies_poster

selected_movie_name=st.selectbox(
    "Select the Movie name",
    movies["title"].values
)



if st.button("Show Recommend"):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])   
    
    
    
    
    
