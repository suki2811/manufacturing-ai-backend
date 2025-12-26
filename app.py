from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Manufacturing Backend Live"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    quantity = data.get("quantity", 100)
    complexity = data.get("complexity", 3)
    material_cost = data.get("material_cost", 40)

    # Simple cost logic
    cost = (material_cost * 0.6) + (complexity * 50) + (1000 / quantity)

    if quantity < 200:
        process = "CNC Machining"
    else:
        process = "Casting"

    return jsonify({
        "estimated_cost": round(cost, 2),
        "recommended_process": process,
        "confidence": "Medium"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

