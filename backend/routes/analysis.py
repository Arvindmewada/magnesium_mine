
from fastapi import APIRouter

from backend.schemas.mining import MiningInput

from backend.services.reserve_service import (
    predict_reserve
)

from backend.services.production_service import (
    predict_production
)

from backend.services.recommendation_service import (
    generate_recommendations
)


router = APIRouter(
    prefix="",
    tags=["Complete Analysis"]
)


@router.post("/analyze")
def complete_analysis(data: MiningInput):

    reserve_result = predict_reserve(data)

    production_result = predict_production(data)

    recommendation_result = generate_recommendations(data)

    return {
        "mine_id": data.mine_id,

        "reserve_prediction": reserve_result,

        "production_prediction": production_result,

        "recommendations": recommendation_result
    }