# Crop Recommendation API

## 📌 Overview
This repository contains a Flask-based API for **Crop Recommendation**. It uses a Machine Learning model to analyze soil and climate parameters and suggests the most suitable crop for cultivation.

The system is designed to help farmers or agricultural planners make data-driven decisions by considering factors like Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall.

## 🚀 Features
- **ML-Powered Recommendations:** Uses a pre-trained model to classify the best crop.
- **REST API:** Accepts JSON input and returns predictions instantly.
- **CORS Enabled:** Configured with `flask-cors` to allow requests from frontend applications (React, Angular, etc.).
- **Cloud Ready:** configured for deployment on platforms like Render (uses port 10000).

## 🛠️ Tech Stack
- **Framework:** Flask (Python)
- **Machine Learning:** Scikit-Learn, Joblib
- **Data Handling:** Pandas, NumPy
- **Server:** Gunicorn

## 📂 File Structure
- `app.py`: Main application file containing the API routes.
- `model.pkl`: *(Required)* The trained machine learning model file.
- `requirements.txt`: Python dependencies.

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
