from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

import os
import numpy as np
from sklearn.linear_model import LinearRegression

MODEL_PATH = "cost_model.pkl"

if not os.path.exists(MODEL_PATH):
    # Train model if it doesn't exist
    X = np.array([
        [10, 1, 50],
        [50, 2, 45],
        [100, 3, 40],
        [500, 4, 35],
        [1000, 5, 30]
    ])
    y = np.array([500, 420, 350, 220, 180])

    temp_model = LinearRegression()
    temp_model.fit(X, y)
    joblib.dump(temp_model, MODEL_PATH)

model = joblib.load(MODEL_PATH)


@app.route("/")
def home():
    return "Manufacturing AI Backend is Live!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    quantity = data["quantity"]
    complexity = data["complexity"]
    material_cost = data["material_cost"]

    prediction = model.predict(
        np.array([[quantity, complexity, material_cost]])
    )[0]

    return jsonify({
        "predicted_cost": round(float(prediction), 2),
        "process": "CNC Machining" if quantity < 200 else "Casting",
        "confidence": "High"
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

