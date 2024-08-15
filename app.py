from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the serialized model
model = joblib.load('./model.joblib')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Claim Amount Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON input data
    data = request.json
    
    # Convert input data into DataFrame
    input_data = pd.DataFrame([data])
    
    # Make prediction using the loaded model
    prediction = model.predict(input_data)
    
    # Return the prediction as JSON
    return jsonify({'predicted_claim_amount': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
