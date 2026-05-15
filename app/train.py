import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os
import mlflow
import mlflow.sklearn

def train_model(data_path="data/movies.csv", model_path="models/model.pkl"):
    print("Starting training...")
    
    # Ensure models directory exists
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    # MLflow Tracking
    mlflow.set_experiment("Movie Recommendation Training")
    
    with mlflow.start_run():
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data file not found at {data_path}")
            
        movies = pd.read_csv(data_path)
        movies['tags'] = movies['genres'] + " " + movies['overview']
        movies['tags'] = movies['tags'].fillna('')
        
        # Log params
        mlflow.log_param("dataset_path", data_path)
        mlflow.log_param("movie_count", len(movies))
        
        # Train TF-IDF
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(movies['tags'])
        
        # Compute Similarity
        similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
        # Save model and data
        model_data = {
            'tfidf': tfidf,
            'tfidf_matrix': tfidf_matrix,
            'similarity_matrix': similarity_matrix,
            'movies': movies
        }
        
        with open(model_path, 'wb') as f:
            pickle.dump(model_data, f)
            
        # Log model to MLflow
        mlflow.sklearn.log_model(tfidf, "tfidf_vectorizer")
        mlflow.log_artifact(model_path)
        
        print(f"Training complete. Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
