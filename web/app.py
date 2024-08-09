import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Function to recommend books based on user input
def recommend(input_word, top_n=5):
    input_vector = tv.transform([input_word])
    cosine_similarities = cosine_similarity(input_vector, vector).flatten()
    top_indices = cosine_similarities.argsort()[-top_n:][::-1]

    for i in top_indices:
        book = books.iloc[i]
        with st.container():
            st.image(book['Book_Image'], width=150)
            st.markdown(f"### {book['Book_Name']}")
            st.markdown(f"**Rating:** 🌟 {book['Book_Rating']}")
            st.markdown(f"**Release Date:** 📅 {book['Book_release_date']}")
            st.markdown(f"**Price:** 💵 Rs. {book['Book_Price']}")
            st.markdown('<hr style="border-top: 1px solid #bbb;">', unsafe_allow_html=True)

# Load the data and vectorizer
books = pickle.load(open('books.pkl', 'rb'))
tv = pickle.load(open('tv.pkl', 'rb'))
vector = tv.transform(books['tags']).toarray()

# Streamlit app layout and design
st.markdown('<h1 style="color:#1f4e79; text-align:center;">📚 Book Recommender System</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#555555; font-size:18px; text-align:center;">Find the perfect book by entering a topic, genre, or author. Let our system guide you to your next great read!</p>', unsafe_allow_html=True)

st.markdown('<hr style="border-top: 2px solid #1f4e79;">', unsafe_allow_html=True)

input_word = st.text_input('🔍 What are you interested in today?', placeholder='Type a keyword, genre, or author here...')

if st.button('Show Recommendations 🚀'):
    if input_word.strip():
        recommend(input_word)
    else:
        st.warning('Please enter a search term to receive recommendations.')

st.markdown('<hr style="border-top: 2px solid #1f4e79;">', unsafe_allow_html=True)

# import streamlit as st
# import pickle
# import pandas as pd
# # from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
#
#
# def recommend(input_word, top_n=5):
#     input_vector = tv.transform([input_word])
#
#     cosine_similarities = cosine_similarity(input_vector, vector).flatten()
#
#     top_indices = cosine_similarities.argsort()[-top_n:][::-1]
#
#     for i in top_indices:
#         st.subheader(books.iloc[i]['Book_Name'])
#         st.image(books.iloc[i]['Book_Image'])
#         st.text('Book Rating : ' + books.iloc[i]['Book_Rating'])
#         st.text('Date of Release : ' + books.iloc[i]['Book_release_date'])
#         st.text('Book Price : Rs.' + books.iloc[i]['Book_Price'])
#         st.markdown('<hr>',
#                     unsafe_allow_html=True)
#
# books = pickle.load(open('books.pkl', 'rb'))
# # vector = pickle.load(open('vector.pkl', 'rb'))
# tv = pickle.load(open('tv.pkl', 'rb'))
# vector = tv.fit_transform(books['tags']).toarray()
# # cosine_similarity = pickle.load(open('cosine_similarity.pkl', 'rb'))
# # tv = CountVectorizer(max_features=6000, stop_words='english')
#
# # book_title = books['Book_Name'].values
#
# st.markdown('<h1 style="color:blue;">Book Recommender System </h1><br><br>',
#             unsafe_allow_html=True)
#
# st.markdown('<h4 style="color:red;">Enter any Topic or Author Name for the search of Best Books</h4>',
#             unsafe_allow_html=True)
#
# input_word = st.text_input('', placeholder='Enter here :')
#
# if st.button('Recommend'):
#     recommend(input_word)
#     # names, image = recommend(input_word)




    # for i in range(0,6):
    #     st.header(names[i])
    #     st.image(image[i])

    # col1, col2, col3, col4, col5 = st.beta_columns(5)
    # with col1:
    #     st.header(names[0])
    #     st.image(image[0])
    # with col2:
    #     st.header(names[1])
    #     st.image(image[1])
    # with col3:
    #     st.header(names[2])
    #     st.image(image[2])
    # with col4:
    #     st.header(names[3])
    #     st.image(image[3])
    # with col5:
    #     st.header(names[4])
    #     st.image(image[4])

