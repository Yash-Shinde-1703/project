from app.recommender import MovieRecommender
import pytest

def test_recommendation_logic():
    recommender = MovieRecommender(data_path="data/movies.csv")
    recs = recommender.get_recommendations("Inception", top_n=2)
    assert len(recs) == 2
    assert "Inception" not in recs

def test_invalid_movie():
    recommender = MovieRecommender(data_path="data/movies.csv")
    recs = recommender.get_recommendations("Unknown Movie")
    assert recs == []
