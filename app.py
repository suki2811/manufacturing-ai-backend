from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

model = joblib.load("cost_model.pkl")

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

