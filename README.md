# VITyarthi_Project-2
Movie Recommendation System: 

OVERVIEW

Choosing a movie from thousands of available options can be overwhelming and time-consuming. This project presents a content-based movie recommendation system that suggests movies based on their similarity in genres.

The system uses machine learning concepts like vectorization and cosine similarity to provide better recommendations compared to basic filtering methods.

PROBLEM

Users often struggle to find movies that match their interests due to the abundance of choices on streaming platforms. A simple and efficient recommendation system can help users discover relevant content quickly.

SOLUTION

This project implements a content-based filtering approach, where:

- Each movie is represented by its genres
- Genres are converted into numerical vectors
- Similarity between movies is calculated using cosine similarity
- Movies with the highest similarity scores are recommended

FEATURES
 Content-based recommendation system
 Uses CountVectorizer for text processing
 Uses cosine similarity for accurate matching
 Fast and efficient recommendations
 Beginner-friendly and easy to understand

 TECH STACK
  Python
  Pandas
  SciKit
  
HOW TO RUN THE PROGRAM

1️) Clone the Repository
     git clone https://github.com/samarth-khare-ok/VITyarthi_Project-2
     cd movie-recommender
2️) Install Dependencies
     pip install -r requirements.txt
3️) Run the Program
     python main.py

How It Works
 Movie genres are converted into vectors using CountVectorizer
 A similarity matrix is created using cosine similarity
 The system finds movies with the highest similarity scores
 Top matching movies are recommended to the user

Advantages
 Does not require user data
 Simple and fast
 Easy to implement and understand
 Scalable with larger datasets

Limitations
 Only considers genres (limited features)
 Does not include user preferences or ratings
 Recommendations may lack personalization 

Future Improvements
 Add user-based collaborative filtering
 Use larger datasets (e.g., TMDB, MovieLens)
 Build a web interface using Streamlit
 Include ratings and reviews for better accuracy

