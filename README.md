# Content-Based Movie Recommendation System

This project is a content based movie recommendation system built using the MovieLens dataset. The system uses machine learning algorithms to recommend movies to users based on their preferences.

## Overview
Content-based movie recommendation is a type of recommendation system that recommends movies to users based on the characteristics (features) of the movies themselves. Unlike collaborative filtering-based recommendation systems, content-based recommendation systems do not take into account the preferences of other users. Instead, they compare the features of the movies available in the dataset to the features of the movie a user has liked or is interested in.

The system consists of three main components:

1. Data preprocessing: This step involves cleaning and preprocessing the MovieLens dataset to prepare it for analysis. The dataset contains information about movies such as their genres, keywords, cast, crew, and directors.

2. Feature extraction: This step involves extracting relevant features from the dataset that can be used to recommend movies. The extracted features are then used to create a similarity matrix that represents the similarity between different movies. The similarity is calculated based on the similarity of their features.

3. Movie recommendation: This step involves using the extracted features and the similarity matrix to recommend movies to users. When a user provides his/her preferences, the system finds the movie that most closely matches the user's preferences. The movie with the highest similarity score is recommended to the user.

Overall, the content-based movie recommendation system is effective for users who have a strong preference for a particular type of movie (e.g., action, comedy, drama, etc.) and are willing to accept a certain level of diversity in their recommendations.

## How to Use
To use the system, follow these steps:
1. Clone the repository.
2. Create a virtual environment (venv or virtualenv) in the project directory.
3. Activate the virtual environment.
4. Install the required dependencies.
   - Run `pip install -r requirements.txt`.
5. Run the `movie-recommendation.py` file to execute the system.
   - If you are using Python 3, you can run `python movie-recommendation.py`.
6. Alternatively, you can run the `movie-recommendation.ipynb` notebook file in Jupyter Notebook/JupyterLab.
7. Enter your movie preferences when prompted.
8. The system will generate movie recommendations based on your preferences.

Note: The system is provided in both `.py` and `.ipynb` file formats.

## Dependencies
The system requires the following dependencies:
- pandas
- numpy
- scikit-learn

## License
This project is licensed under the MIT License. See the LICENSE file for more details.


## Visit and Follow
For more details and tutorials, visit the website: [DocsAllOver](https://docsallover.com/).

Follow us on:
- [Facebook](https://www.facebook.com/docsallover)
- [Instagram](https://www.instagram.com/docsallover.tech/)
- [LinkedIn](https://www.linkedin.com/company/docsallover/)
- [YouTube](https://www.youtube.com/@docsallover)
- [Threads.net](https://threads.net/docsallover.tech)

and visit our website to know more about our tutorials and blogs.
