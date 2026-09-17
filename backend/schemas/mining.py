from pydantic import BaseModel


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