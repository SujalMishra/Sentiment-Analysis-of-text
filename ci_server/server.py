from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
import joblib 
import tensorflow as tf
import keras
# from tensorflow.keras.models import load_model


# print("TensorFlow version: ", tf.__version__)
# print("keras:" ,keras.__version__)
app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Load vectorizer and model
vectorizer = joblib.load("vectorizer.pkl")
# model1 = joblib.load("ann_pkl")
# model2 = joblib.load("bert_pkl")
model3 = joblib.load("logreg_model.pkl")
# model4 = joblib.load("cnn_pkl")
# model5 = joblib.load("lstm_pkl")
# model6 = joblib.load("resnet_pkl")

# model1 = keras.models.load_model('ann_pkl.pkl')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.json
        comment = data.get('comment')
        comment_vector = vectorizer.transform([comment])

        # List to hold results from all models
        results = []

        # Predict sentiment using each model and append the result to the results list
        models = [  model3]
        for model in models:
            sentiment = model.predict(comment_vector)[0]
            if sentiment == 1:
                results.append('positive')
            elif sentiment == 0:
                results.append('neutral')
            elif sentiment == -1:
                results.append('negative')
            else:
                results.append('unknown')  # In case the model returns an unexpected value

        # Return all results as a JSON array
        return jsonify({'results': results})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
