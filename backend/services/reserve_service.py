
from backend.schemas.mining import MiningInput


def predict_reserve(data: MiningInput):

    # TEMPORARY MOCK LOGIC
    # Person 3 ka real ML model baad mein connect hoga.

    if data.ore_grade >= 30:
        potential = "HIGH"

    elif data.ore_grade >= 15:
        potential = "MEDIUM"

    else:
        potential = "LOW"

    predicted_reserve = (
        5000
        + (data.ore_grade * 200)
        + (data.drilling_depth * 10)
    )

    return {
        "mine_id": data.mine_id,
        "predicted_reserve_tonnes": round(
            predicted_reserve, 2
        ),
        "predicted_grade_percent": data.ore_grade,
        "reserve_potential": potential
    }