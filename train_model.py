import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Sample synthetic manufacturing data
# [quantity, complexity, material_cost]
X = np.array([
    [10, 1, 50],
    [50, 2, 45],
    [100, 3, 40],
    [500, 4, 35],
    [1000, 5, 30]
])

# Cost per unit
y = np.array([500, 420, 350, 220, 180])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "cost_model.pkl")
print("Model trained and saved")
