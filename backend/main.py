from fastapi import FastAPI
from pydantic import BaseModel


# ==========================================
# MOIL AI MINING API
# ==========================================

app = FastAPI(
    title="MOIL AI Mining API",
    description="AI/ML based Manganese Mining System",
    version="1.0.0"
)


# ==========================================
# INPUT DATA MODEL
# ==========================================

class MiningInput(BaseModel):
    mine_id: str

    latitude: float
    longitude: float

    rainfall: float = 0.0
    soil_moisture: float = 0.0
    land_temperature: float = 0.0
    ndvi: float = 0.0

    drilling_depth: float = 0.0
    ore_grade: float = 0.0

    equipment_downtime: float = 0.0
    blasting_delay: float = 0.0

    historical_production: float = 0.0
    production_target: float = 0.0


# ==========================================
# HOME API
# ==========================================

@app.get("/")
def root():
    return {
        "message": "MOIL AI Mining API is running",
        "status": "success"
    }


# ==========================================
# HEALTH CHECK API
# ==========================================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "MOIL AI Mining API"
    }


# ==========================================
# RESERVE PREDICTION API
# ==========================================

@app.post("/predict/reserve")
def predict_reserve(data: MiningInput):

    # TEMPORARY MOCK LOGIC
    # Person 3 ka real ML model baad mein yahan connect hoga.

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
        "predicted_reserve_tonnes": round(predicted_reserve, 2),
        "predicted_grade_percent": data.ore_grade,
        "reserve_potential": potential
    }


# ==========================================
# PRODUCTION PREDICTION API
# ==========================================

@app.post("/predict/production")
def predict_production(data: MiningInput):

    # TEMPORARY MOCK LOGIC
    # Person 4 ka real ML model baad mein connect hoga.

    predicted_production = data.historical_production

    # Equipment downtime effect
    predicted_production -= (
        data.historical_production
        * data.equipment_downtime
        / 100
    )

    # Blasting delay effect
    predicted_production -= (
        data.historical_production
        * data.blasting_delay
        / 100
    )

    predicted_production = max(
        0,
        predicted_production
    )

    # Calculate shortfall
    shortfall = max(
        0,
        data.production_target
        - predicted_production
    )

    # Calculate shortfall percentage
    if data.production_target > 0:
        shortfall_percentage = (
            shortfall
            / data.production_target
        ) * 100
    else:
        shortfall_percentage = 0

    # Risk classification
    if shortfall_percentage > 15:
        risk = "HIGH"

    elif shortfall_percentage > 5:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    return {
        "mine_id": data.mine_id,
        "target_production_tonnes": round(
            data.production_target, 2
        ),
        "predicted_production_tonnes": round(
            predicted_production, 2
        ),
        "expected_shortfall_tonnes": round(
            shortfall, 2
        ),
        "shortfall_percentage": round(
            shortfall_percentage, 2
        ),
        "shortfall_risk": risk
    }


# ==========================================
# RECOMMENDATION API
# ==========================================

@app.post("/recommend")
def recommend(data: MiningInput):

    recommendations = []

    # Equipment problem
    if data.equipment_downtime > 15:

        recommendations.append({
            "problem": "High equipment downtime",
            "action": "Re-deploy available equipment",
            "priority": "HIGH"
        })

    # Weather problem
    if data.rainfall > 50:

        recommendations.append({
            "problem": "Heavy rainfall",
            "action": "Adjust mining schedule",
            "priority": "MEDIUM"
        })

    # Blasting problem
    if data.blasting_delay > 10:

        recommendations.append({
            "problem": "Blasting delay",
            "action": "Reschedule blasting operations",
            "priority": "HIGH"
        })

    # High grade ore
    if data.ore_grade >= 30:

        recommendations.append({
            "problem": "High-grade ore zone identified",
            "action": "Prioritize high-potential mining zone",
            "priority": "HIGH"
        })

    # No problem
    if not recommendations:

        recommendations.append({
            "problem": "No major risk detected",
            "action": "Continue current mining plan",
            "priority": "LOW"
        })

    return {
        "mine_id": data.mine_id,
        "recommendations": recommendations
    }


# ==========================================
# COMPLETE ANALYSIS API
# ==========================================

@app.post("/analyze")
def analyze(data: MiningInput):

    # --------------------------------------
    # 1. RESERVE PREDICTION
    # --------------------------------------

    if data.ore_grade >= 30:
        reserve_potential = "HIGH"

    elif data.ore_grade >= 15:
        reserve_potential = "MEDIUM"

    else:
        reserve_potential = "LOW"

    predicted_reserve = (
        5000
        + (data.ore_grade * 200)
        + (data.drilling_depth * 10)
    )

    # --------------------------------------
    # 2. PRODUCTION PREDICTION
    # --------------------------------------

    predicted_production = data.historical_production

    predicted_production -= (
        data.historical_production
        * data.equipment_downtime
        / 100
    )

    predicted_production -= (
        data.historical_production
        * data.blasting_delay
        / 100
    )

    predicted_production = max(
        0,
        predicted_production
    )

    # --------------------------------------
    # 3. SHORTFALL CALCULATION
    # --------------------------------------

    shortfall = max(
        0,
        data.production_target
        - predicted_production
    )

    if data.production_target > 0:

        shortfall_percentage = (
            shortfall
            / data.production_target
        ) * 100

    else:

        shortfall_percentage = 0

    # --------------------------------------
    # 4. RISK LEVEL
    # --------------------------------------

    if shortfall_percentage > 15:
        risk = "HIGH"

    elif shortfall_percentage > 5:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    # --------------------------------------
    # 5. RECOMMENDATIONS
    # --------------------------------------

    recommendations = []

    if data.equipment_downtime > 15:

        recommendations.append(
            "Re-deploy available equipment"
        )

    if data.rainfall > 50:

        recommendations.append(
            "Adjust mining schedule due to rainfall"
        )

    if data.blasting_delay > 10:

        recommendations.append(
            "Reschedule blasting operations"
        )

    if reserve_potential == "HIGH":

        recommendations.append(
            "Prioritize high-potential reserve zone"
        )

    if not recommendations:

        recommendations.append(
            "Continue current mining plan"
        )

    # --------------------------------------
    # FINAL RESPONSE
    # --------------------------------------

    return {

        "mine_id": data.mine_id,

        "reserve_prediction": {

            "predicted_reserve_tonnes": round(
                predicted_reserve,
                2
            ),

            "predicted_grade_percent": data.ore_grade,

            "potential": reserve_potential
        },

        "production_prediction": {

            "target_tonnes": round(
                data.production_target,
                2
            ),

            "predicted_tonnes": round(
                predicted_production,
                2
            ),

            "shortfall_tonnes": round(
                shortfall,
                2
            ),

            "shortfall_percentage": round(
                shortfall_percentage,
                2
            )
        },

        "risk": {

            "level": risk
        },

        "recommendations": recommendations
    }