# SAFE-SENSE-AI
# 🚨 AI-Based Women Safety Risk Assessment System

## 📌 Overview

This project is a **real-time AI-powered web application** designed to enhance personal safety by analyzing user-described situations and predicting risk levels (**Safe / Danger**) using **Natural Language Processing (NLP)** and **Machine Learning**.

It also integrates **location tracking, voice input, and emergency response features** to provide immediate assistance during potentially unsafe situations.

---

## 🎯 Key Features

### 🧠 AI Risk Detection

* Uses **TF-IDF + Logistic Regression** for text classification
* Predicts:

  * Risk Level (**Safe / Danger**)
  * Risk Score (probability)

---

### 🎤 Voice Interaction

* Voice input using **Web Speech API**
* **Panic Mode**: detects keywords like *“help”, “danger”*
* Automatically triggers emergency actions

---

### 📍 Location Tracking

* Uses **Geolocation API**
* Displays real-time position on map using **Leaflet + OpenStreetMap**

---

### 🚨 Emergency System

* One-click **Emergency Call**
* **SMS alert with live location**
* Voice-triggered emergency activation

---

### 📊 Interactive UI

* Responsive design (mobile + desktop)
* Risk visualization using progress bar
* Clean and structured layout

---

## 🛠️ Tech Stack

### 🔹 Frontend

* HTML5
* CSS3 (Responsive Design, Grid Layout)
* JavaScript (ES6)

### 🔹 Backend

* Python
* Flask

### 🔹 Machine Learning

* Scikit-learn

  * TF-IDF Vectorizer
  * Logistic Regression

### 🔹 Libraries

* Pandas
* NumPy
* Pickle

### 🔹 Maps & Location

* Leaflet.js
* OpenStreetMap
* Geolocation API

### 🔹 Voice Processing

* Web Speech API

---

## 📁 Project Structure

```
women_safety_ai/
│
├── app.py                 # Flask backend
├── model.py               # Model training script
├── dataset.csv            # Training dataset
├── model.pkl              # Trained ML model
├── vectorizer.pkl         # TF-IDF vectorizer
│
└── templates/
    └── index.html         # Frontend UI
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/women-safety-ai.git
cd women-safety-ai
```

---

### 2️⃣ Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

---

### 3️⃣ Train Model

```bash
python model.py
```

---

### 4️⃣ Run Application

```bash
python app.py
```

---

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🧪 Example Inputs

### 🔴 Danger

* “Help! I am being followed”
* “Someone is trying to attack me”

### 🟢 Safe

* “I am at home and everything is fine”
* “Walking safely in a crowded area”

---

## 🚀 Future Enhancements

* 📲 WhatsApp emergency alerts
* 📡 Real-time live location sharing
* 🧠 Deep learning models (LSTM/BERT)
* 📱 Mobile app version (Android/iOS)
* ☁️ Cloud deployment with user authentication

---

## 🎓 Use Case

This system can be used for:

* Personal safety assistance
* Smart city surveillance support
* Emergency alert systems
* AI-based risk monitoring tools

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is for academic and educational purposes.

---

## ⭐ Acknowledgment

Inspired by the need for smarter, AI-driven safety solutions in real-world scenarios.
