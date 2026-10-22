
from pathlib import Path

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load Iris dataset
X, y = load_iris(return_X_y=True)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model in the same folder as this file
model_path = Path(__file__).with_name("model.pkl")
joblib.dump(model, model_path)

print(f"Model saved successfully at: {model_path}")
