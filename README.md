# Movie Recommendation System

A robust MLOps pipeline for a movie recommendation system using FastAPI, Next.js, DVC, and MLflow.

## Project Structure

- `app/`: FastAPI backend implementation.
  - `main.py`: API endpoints.
  - `recommender.py`: Movie recommendation logic with MLflow tracking.
- `frontend/`: Next.js frontend application.
- `data/`: Dataset for movie recommendations (versioned with DVC).
- `tests/`: Automated tests for backend and logic.
- `.github/workflows/`: CI/CD pipeline configuration.

## Getting Started

### Local Setup with Docker Compose

1. **Clone the repository.**
2. **Run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```
3. **Access the services:**
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend API: [http://localhost:8000](http://localhost:8000)
   - MLflow UI: [http://localhost:5000](http://localhost:5000)

### Manual Setup (Development)

#### Backend
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the backend: `python -m app.main`

#### Frontend
1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Run the development server: `npm run dev`

## MLOps Pipeline

### Data Versioning (DVC)
Data is managed using DVC. To pull the latest data:
```bash
dvc pull
```

### Experiment Tracking (MLflow)
The system uses MLflow to track model initialization and recommendation metrics.

### CI/CD
The GitHub Actions pipeline automates:
- Testing and Linting
- Docker Image Building and Pushing to Docker Hub
- (Optional) Deployment to production

## License
MIT
