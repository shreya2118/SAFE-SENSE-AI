from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Dummy tips
def get_tips(label):
    if label == "danger":
        return [
            "Move to a safe location immediately",
            "Contact trusted person",
            "Call emergency services",
            "Stay alert and aware"
        ]
    else:
        return [
            "Stay aware of surroundings",
            "Keep emergency contacts ready"
        ]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")

    X = vectorizer.transform([text])

    probs = model.predict_proba(X)[0]
    danger_index = list(model.classes_).index("danger")

    danger_prob = probs[danger_index]

    prediction = "danger" if danger_prob > 0.5 else "safe"

    return jsonify({
        "prediction": prediction,
        "risk_score": float(danger_prob),
        "recommendations": ["Stay alert", "Contact someone if needed"]
    })



if __name__ == "__main__":
    app.run(debug=True)