import datetime

def context_risk_boost(base_score, location=None):
    hour = datetime.datetime.now().hour

    # Night risk
    if hour >= 21 or hour <= 5:
        base_score += 0.15

    # Example: unsafe zone (mock logic)
    if location:
        lat, lon = location
        if lat > 28.6:  # dummy condition
            base_score += 0.1

    return min(base_score, 1.0)
def get_risk_score(probs):
    # probability of danger class
    danger_prob = probs[1]
    return float(danger_prob)

def get_safety_tips(label):
    if label == "danger":
        return [
            "Move to a crowded place",
            "Call emergency contact",
            "Enable GPS tracking"
        ]
    return ["You are safe"]

