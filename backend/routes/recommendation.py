
from fastapi import APIRouter

from backend.schemas.mining import MiningInput

from backend.services.recommendation_service import (
    generate_recommendations
)


router = APIRouter(
    prefix="",
    tags=["AI Recommendations"]
)


@router.post("/recommend")
def recommend(data: MiningInput):

    result = generate_recommendations(data)

    return result