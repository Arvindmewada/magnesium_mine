
from fastapi import APIRouter

from backend.schemas.mining import MiningInput

from backend.services.production_service import (
    predict_production
)


router = APIRouter(
    prefix="/predict",
    tags=["Production Prediction"]
)


@router.post("/production")
def production_prediction(data: MiningInput):

    result = predict_production(data)

    return result