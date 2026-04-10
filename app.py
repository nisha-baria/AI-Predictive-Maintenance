from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("models/model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    input_data = np.array([[data['temperature'], data['vibration'], data['current']]])

    prediction = model.predict(input_data)[0]

    result = "FAILURE" if prediction == 1 else "NORMAL"

    return jsonify({"prediction": result})

app.run(debug=True)