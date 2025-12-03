from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model
# Ensure 'crop_recommendation_model.pkl' is in the same folder as this script
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "Crop Recommendation API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # specific feature order required by the model
        feature_order = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
        
        # Convert dictionary to DataFrame (handling single input)
        if isinstance(data, dict):
            # Check if all keys exist
            if not all(key in data for key in feature_order):
                return jsonify({'error': f'Missing features. Required: {feature_order}'}), 400
            
            input_data = pd.DataFrame([data])
        elif isinstance(data, list):
            input_data = pd.DataFrame(data)
        else:
            return jsonify({'error': 'Invalid input format. Send a JSON object or list.'}), 400

        # Ensure correct column order
        input_data = input_data[feature_order]

        # Make prediction
        prediction = model.predict(input_data)
        
        # Return result
        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
