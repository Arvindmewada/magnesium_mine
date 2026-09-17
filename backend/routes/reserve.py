from fastapi import APIRouter
from backend.schemas.mining import MiningInput
from backend.services.reserve_service import predict_reserve

router = APIRouter(
    prefix="/predict",
    tags=["Reserve Prediction"]
)


@router.post("/reserve")
def reserve_prediction(data: MiningInput):
    result = predict_reserve(data)
    return result