import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import mlflow

class MovieRecommender:
    def __init__(self, data_path="data/movies.csv"):
        self.data_path = data_path
        self.movies = None
        self.similarity_matrix = None
        
        # MLflow Tracking
        mlflow.set_experiment("Movie Recommendation")
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        
        with mlflow.start_run(run_name="Model Initialization"):
            self.movies = pd.read_csv(self.data_path)
            # Create tags by combining genres and overview
            self.movies['tags'] = self.movies['genres'] + " " + self.movies['overview']
            self.movies['tags'] = self.movies['tags'].fillna('')
            
            # Log metrics and params
            mlflow.log_param("dataset_path", self.data_path)
            mlflow.log_metric("movie_count", len(self.movies))
            
            # Initialize TF-IDF Vectorizer
            tfidf = TfidfVectorizer(stop_words='english')
            tfidf_matrix = tfidf.fit_transform(self.movies['tags'])
            
            # Compute Cosine Similarity
            self.similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
            mlflow.log_param("vectorizer", "TfidfVectorizer")
            mlflow.log_param("similarity_metric", "cosine_similarity")

    def get_recommendations(self, title, top_n=5):
        if self.movies is None:
            self.load_data()
            
        # Find the index of the movie that matches the title
        try:
            idx = self.movies[self.movies['title'].str.lower() == title.lower()].index[0]
        except IndexError:
            return []

        # Get the pairwise similarity scores of all movies with that movie
        sim_scores = list(enumerate(self.similarity_matrix[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the top_n most similar movies (excluding itself)
        sim_scores = sim_scores[1:top_n+1]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top_n most similar movies
        return self.movies['title'].iloc[movie_indices].tolist()

if __name__ == "__main__":
    recommender = MovieRecommender()
    print(recommender.get_recommendations("Inception"))
