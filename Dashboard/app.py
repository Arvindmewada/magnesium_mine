
import streamlit as st
import requests

st.set_page_config(
    page_title="MOIL AI Mining Dashboard",
    page_icon="⛏️",
    layout="wide"
)

st.title("⛏️ MOIL AI Mining Dashboard")
st.caption("AI/ML Based Manganese Mining Analysis")

API_URL = "http://127.0.0.1:8000"

st.sidebar.header("Mine Input")

mine_id = st.sidebar.text_input(
    "Mine ID",
    "MOIL-01"
)

latitude = st.sidebar.number_input(
    "Latitude",
    value=21.90
)

longitude = st.sidebar.number_input(
    "Longitude",
    value=80.10
)

rainfall = st.sidebar.number_input(
    "Rainfall",
    value=10.0
)

soil_moisture = st.sidebar.number_input(
    "Soil Moisture",
    value=42.0
)

land_temperature = st.sidebar.number_input(
    "Land Temperature",
    value=31.0
)

ndvi = st.sidebar.number_input(
    "NDVI",
    value=0.45
)

drilling_depth = st.sidebar.number_input(
    "Drilling Depth",
    value=150.0
)

ore_grade = st.sidebar.number_input(
    "Ore Grade (%)",
    value=32.0
)

equipment_downtime = st.sidebar.number_input(
    "Equipment Downtime",
    value=18.0
)

blasting_delay = st.sidebar.number_input(
    "Blasting Delay",
    value=12.0
)

historical_production = st.sidebar.number_input(
    "Historical Production",
    value=10000.0
)

production_target = st.sidebar.number_input(
    "Production Target",
    value=10000.0
)

if st.button("🔍 Analyze Mine"):

    payload = {
        "mine_id": mine_id,
        "latitude": latitude,
        "longitude": longitude,
        "rainfall": rainfall,
        "soil_moisture": soil_moisture,
        "land_temperature": land_temperature,
        "ndvi": ndvi,
        "drilling_depth": drilling_depth,
        "ore_grade": ore_grade,
        "equipment_downtime": equipment_downtime,
        "blasting_delay": blasting_delay,
        "historical_production": historical_production,
        "production_target": production_target
    }

    try:

        response = requests.post(
            f"{API_URL}/analyze",
            json=payload,
            timeout=10
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Analysis completed successfully!")

            reserve = result.get(
                "reserve_prediction", {}
            )

            production = result.get(
                "production_prediction", {}
            )

            recommendations = result.get(
                "recommendations", {}
            )

            st.subheader("📊 Mining Overview")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Predicted Reserve",
                    reserve.get(
                        "predicted_reserve_tonnes",
                        "N/A"
                    )
                )

            with col2:
                st.metric(
                    "Predicted Production",
                    production.get(
                        "predicted_production_tonnes",
                        "N/A"
                    )
                )

            with col3:
                st.metric(
                    "Shortfall Risk",
                    production.get(
                        "risk_level",
                        "N/A"
                    )
                )

            st.subheader("📦 Reserve Prediction")
            st.json(reserve)

            st.subheader("🏭 Production Prediction")
            st.json(production)

            st.subheader("🤖 AI Recommendations")

            if isinstance(recommendations, dict):

                st.write(
                    recommendations.get(
                        "recommendations",
                        []
                    )
                )

            else:
                st.write(recommendations)

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

            st.code(response.text)

    except requests.exceptions.ConnectionError:

        st.error(
            "Backend is not running. Start FastAPI first."
        )

    except requests.exceptions.RequestException as e:

        st.error(f"Request failed: {e}")