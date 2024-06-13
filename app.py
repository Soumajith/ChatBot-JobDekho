from flask import Flask, request, jsonify, render_template
import pandas as pd
from flask_cors import CORS  # CORS for handling Cross-Origin Resource Sharing
import pickle 

# Create a Flask application instance
app = Flask(__name__)

# Enable CORS for all routes, allowing requests from any origin
CORS(app, resources={r"/*": {"origins": "*"}})

# Load the trained model
model = pickle.load(open('job_portal_model.pkl', 'rb'))

# Define a route for handling HTTP GET requests to the root URL
@app.route('/', methods=['GET'])
def get_data():
    return render_template('index.html')

# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the POST request
        data = request.get_json()
        
        # Extract the user input text
        user_input = data['User Input']
        
        # Create a DataFrame from the input
        query_df = pd.DataFrame([user_input], columns=['User Input'])
        
        # Make a prediction using the model
        prediction = model.predict(query_df['User Input'])
        
        # Return the prediction as a JSON response
        return jsonify({'Prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
