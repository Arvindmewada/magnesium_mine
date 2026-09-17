from fastapi import FastAPI

from backend.routes.analysis import router as analysis_router
from backend.routes.production import router as production_router
from backend.routes.recommendation import router as recommendation_router
from backend.routes.reserve import router as reserve_router


app = FastAPI(
    title="MOIL AI Mining API",
    description="AI/ML based Manganese Mining System",
    version="1.0.0",
)

app.include_router(reserve_router)
app.include_router(production_router)
app.include_router(recommendation_router)
app.include_router(analysis_router)


@app.get("/")
def root():
    return {
        "message": "MOIL AI Mining API is running",
        "status": "success",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "MOIL AI Mining API",
    }