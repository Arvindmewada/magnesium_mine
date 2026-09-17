
from backend.schemas.mining import MiningInput


def generate_recommendations(data: MiningInput):

    recommendations = []

    if data.equipment_downtime >= 15:
        recommendations.append(
            "Re-deploy backup equipment to reduce downtime"
        )

    if data.blasting_delay >= 10:
        recommendations.append(
            "Review and reschedule blasting operations"
        )

    if data.rainfall >= 50:
        recommendations.append(
            "Adjust mining schedule due to heavy rainfall"
        )

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

    shortfall = max(
        0,
        target - predicted_production
    )

    shortfall_percentage = (
        shortfall / target
    ) * 100

    if shortfall_percentage >= 30:
        risk = "HIGH"
    elif shortfall_percentage >= 15:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    if not recommendations:
        recommendations.append(
            "Continue regular monitoring and production planning"
        )

    return {
        "mine_id": data.mine_id,
        "risk_level": risk,
        "shortfall_percentage": round(
            shortfall_percentage, 2
        ),
        "recommendations": recommendations
    }