from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.recommender import MovieRecommender
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Movie Recommendation System", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

recommender = MovieRecommender()

class RecommendationRequest(BaseModel):
    movie_title: str
    top_n: int = 5

class RecommendationResponse(BaseModel):
    recommendations: List[str]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/recommend", response_model=RecommendationResponse)
def recommend(request: RecommendationRequest):
    recommendations = recommender.get_recommendations(request.movie_title, request.top_n)
    if not recommendations:
        raise HTTPException(status_code=404, detail="Movie not found in dataset")
    return {"recommendations": recommendations}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
