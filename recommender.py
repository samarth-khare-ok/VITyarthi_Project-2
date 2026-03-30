# recommender.py

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
def load_data():
    return pd.read_csv("data/movies.csv")

# Create similarity matrix
def create_similarity():
    data = load_data()
    
    # Convert genre text into vectors
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['genre'])
    
    # Compute similarity
    similarity = cosine_similarity(count_matrix)
    
    return data, similarity

# Recommend function
def recommend(movie_name):
    data, similarity = create_similarity()
    
    if movie_name not in data['title'].values:
        print("Movie not found!")
        return
    
    idx = data[data['title'] == movie_name].index[0]
    
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    print(f"\nBecause you watched '{movie_name}', you may also like:\n")
    
    for i in scores[1:6]:
        print(data.iloc[i[0]].title)
