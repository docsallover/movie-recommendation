import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movie_dataset.csv")
df.head()
df.describe()
#print(df.columns.values)
features = ['genres', 'keywords', 'title', 'cast', 'director']
df['cast'].isnull().values.any()


def combine_features(row):
    return row['title']+' '+row['genres']+' '+row['director']+' '+row['keywords']+' '+row['cast']


for feature in features:
    df[feature] = df[feature].fillna('')

df['combined_features'] = df.apply(combine_features, axis = 1)

#print(df.loc[0, 'combined_features'])

cv = CountVectorizer()
count_matrix = cv.fit_transform(df['combined_features'])
cosine_sim = cosine_similarity(count_matrix)

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


movie_user_likes = input("Enter your favourite movie: ")
try:
    movie_index = get_index_from_title(movie_user_likes)
except:
    print("Movie Not Found/Spelling Incorrect/Not in dataset/Capitalisation Incorrect")    
    exit()

similar_movies = list(enumerate(cosine_sim[movie_index])) #accessing the row corresponding to given movie to find all the similarity scores for that movie and then enumerating over it
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]

i=0
print("Top 10 similar movies to "+movie_user_likes+" are:\n")
for element in sorted_similar_movies:
    print(get_title_from_index(element[0]))
    i=i+1
    if i>10:
        break