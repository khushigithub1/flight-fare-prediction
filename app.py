import os
import pickle
from datetime import datetime

import numpy as np
import pandas as pd
from flask import Flask, render_template, request

# ==========================================================
# App setup
# ==========================================================

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH    = os.path.join(BASE_DIR, "models", "model.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "models", "features.pkl")
SCALER_PATH   = os.path.join(BASE_DIR, "models", "scaler.pkl")


def load_models():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(FEATURES_PATH, "rb") as f:
        features = pickle.load(f)
    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)
    return model, features, scaler


model, features, scaler = load_models()


# ==========================================================
# Routes
# ==========================================================

@app.route("/")
def index():
    return render_template("index.html", prediction=None)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # ---- Collect form values ----
        airline      = request.form.get("airline", "")
        source       = request.form.get("source", "")
        destination  = request.form.get("destination", "")
        stops_raw    = request.form.get("stops", "Non-Stop")
        journey_date = request.form.get("journey_date", "")
        dep_time     = request.form.get("dep_time", "00:00")
        arr_time     = request.form.get("arr_time", "00:00")

        # ---- Derive numeric features ----
        stops_map = {
            "Non-Stop": 0,
            "1 Stop":   1,
            "2 Stops":  2,
            "3 Stops":  3,
        }
        total_stops = stops_map.get(stops_raw, 0)

        date_obj      = datetime.strptime(journey_date, "%Y-%m-%d")
        journey_day   = date_obj.day
        journey_month = date_obj.month

        dep_h, dep_m = map(int, dep_time.split(":"))
        arr_h, arr_m = map(int, arr_time.split(":"))
        total_dep  = dep_h * 60 + dep_m
        total_arr  = arr_h * 60 + arr_m
        diff_min   = total_arr - total_dep
        if diff_min < 0:
            diff_min += 1440          # overnight flight

        duration_hours   = diff_min // 60
        duration_minutes = diff_min % 60

        # ---- Build feature DataFrame ----
        input_data = pd.DataFrame(0, index=[0], columns=features)

        num_map = {
            "Total_Stops":       total_stops,
            "Journey_Day":       journey_day,
            "Journey_Month":     journey_month,
            "Duration_hours":    duration_hours,
            "Duration_minutes":  duration_minutes,
        }
        for col, val in num_map.items():
            if col in input_data.columns:
                input_data[col] = val

        for prefix, value in [
            ("Airline_",     airline),
            ("Source_",      source),
            ("Destination_", destination),
        ]:
            col = f"{prefix}{value}"
            if col in input_data.columns:
                input_data[col] = 1

        input_data    = input_data[features]
        input_scaled  = scaler.transform(input_data)
        raw_pred      = model.predict(input_scaled)
        predicted_fare = float(np.asarray(raw_pred).flatten()[0])

        return render_template(
            "index.html",
            prediction=f"{predicted_fare:,.2f}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction=None,
            error=str(e)
        )


# ==========================================================
# Entry point
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True, port=5000)
