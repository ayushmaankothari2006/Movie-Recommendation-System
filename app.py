import streamlit as st
#import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # fetched index of movie
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)  # i[0] is movie index
    return recommended_movies

#extra step to create data frame
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity =  pickle.load(open('similarity.pkl','rb'))#importing similarity file

st.title('Movie Recommender System')
##terminal: streamlit run app.py
#its a running command

selected_movie_name = st.selectbox(
'select movie to recommend:',
movies['title'].values)
#indirect code but yes , bec. it isn't loading directly

#Code for button
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

#   ======================================
#   EXTRA COMMANDS TO KEEP PROGRAM RUN:
#   1. navigate to your project deployer folder in terminal
#   2. create the virtual environment
#   python -m venv myenv
#   3. activate the virtual environment
#   source DEPLOYER/myenv/bin/activate
#   or
#   source myenv/bin/activate
#   4. check pip contents(if already contain streamlit, and other libraries, then skip next point)
#   pip list
#   5.  download libraries
#   pip install streamlit pickle
#   6. recheck
#   pip list
#   7. run library
#   streamlit run app.py
#   ======================================
