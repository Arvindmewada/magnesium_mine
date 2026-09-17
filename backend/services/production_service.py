
from backend.schemas.mining import MiningInput


def predict_production(data: MiningInput):

    target = data.production_target

    if target <= 0:
        target = 10000

    predicted_production = (
        data.historical_production
        - (data.equipment_downtime * 20)
        - (data.blasting_delay * 15)
        - (data.rainfall * 2)
    )

    predicted_production = max(
        0,
        predicted_production
    )

    shortfall_tonnes = max(
        0,
        target - predicted_production
    )

    shortfall_percentage = (
        shortfall_tonnes / target
    ) * 100

    if shortfall_percentage >= 30:
        risk = "HIGH"

    elif shortfall_percentage >= 15:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    return {
        "mine_id": data.mine_id,
        "production_target_tonnes": round(target, 2),
        "predicted_production_tonnes": round(
            predicted_production, 2
        ),
        "shortfall_tonnes": round(
            shortfall_tonnes, 2
        ),
        "shortfall_percentage": round(
            shortfall_percentage, 2
        ),
        "risk_level": risk
    }