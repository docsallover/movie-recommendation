"""
Content-Based Movie Recommendation System
This project is a content based movie recommendation system built using the MovieLens dataset. The system uses machine learning algorithms to recommend movies to users based on their preferences.
Created By : [DocsAllOver](https://docsallover.com/)
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read the CSV file containing movie data
df = pd.read_csv("movie_dataset.csv")

# Display the first few rows of the data
df.head()

# Display the statistical summary of the data
df.describe()

# Print the column names of the data
# print(df.columns.values)

# List of features to be considered for recommendation
features = ["genres", "keywords", "title", "cast", "director"]

# Check if there are any NaN values in the 'cast' column
df["cast"].isnull().values.any()


def combine_features(row):
    """
    Combine various features of a movie into a single string
    """
    return (
        row["title"] + " " + row["genres"] + " " + row["director"] + " " + row["keywords"] + " " + row["cast"]
    )

# Fill NaN values in the specified columns with empty string
for feature in features:
    df[feature] = df[feature].fillna("")

# Combine the features for each movie into a single 'combined_features' column
df["combined_features"] = df.apply(combine_features, axis=1)

# Vectorize the 'combined_features' column
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(count_matrix)


def get_title_from_index(index):
    """
    Get the title of a movie from its index
    """
    return df[df.index == index]["title"].values[0]


def get_index_from_title(title):
    """
    Get the index of a movie from its title
    """
    return df[df.title == title]["index"].values[0]


# Get the user's favorite movie
movie_user_likes = input("Enter your favourite movie: ")
try:
    movie_index = get_index_from_title(movie_user_likes)
except:
    print("Movie Not Found/Spelling Incorrect/Not in dataset/Capitalisation Incorrect")
    exit()

# Find the most similar movies to the user's favorite movie
similar_movies = list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

# Print the top 10 similar movies
i = 0
print("Top 10 similar movies to " + movie_user_likes + " are:\n")
for element in sorted_similar_movies:
    print(get_title_from_index(element[0]))
    i = i + 1
    if i > 10:
        break
