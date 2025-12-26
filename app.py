from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# FULL CORS CONFIG (THIS IS THE FIX)
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True
)

@app.route("/", methods=["GET"])
def home():
    return "Manufacturing Backend Live"

@app.route("/predict", methods=["POST", "OPTIONS"])
def predict():
    if request.method == "OPTIONS":
        # Preflight request
        return "", 200

    data = request.get_json(force=True)

    quantity = data.get("quantity", 100)
    complexity = data.get("complexity", 3)
    material_cost = data.get("material_cost", 40)

    cost = (material_cost * 0.6) + (complexity * 50) + (1000 / quantity)

    process = "CNC Machining" if quantity < 200 else "Casting"

    return jsonify({
        "estimated_cost": round(cost, 2),
        "recommended_process": process,
        "confidence": "Medium"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


