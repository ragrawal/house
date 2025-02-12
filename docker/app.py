import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load your model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data['features']  # Assuming your input is a list of features

    # Make prediction
    prediction = model.predict([features]) 

    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)