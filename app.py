import streamlit as st
import pickle
import requests
def fetch_posters(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=539d2d5bdfab55d9f5636de376fa0c21&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    if poster_path is False:
        poster_path="/m73KqOLXf9ZvPVCWS5dz5Hv7yQF.jpg"
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_ind=movies[movies['title']==movie].index[0]
    distance=similarity[movie_ind]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        # now fetch posters to display form TMDB API
        recommended_movies_poster.append(fetch_posters(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies,recommended_movies_poster


movies_list=pickle.load(open('movies.pkl','rb'))
movies=movies_list
movies_list=movies_list['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommendation System")
selected_movie_title=st.selectbox('Choose your favourite movie',movies_list)

if st.button('Recommend'):
    name,poster=recommend(selected_movie_title)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])