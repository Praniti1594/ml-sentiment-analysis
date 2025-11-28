from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load vectorizer + best model (Logistic Regression)
vectorizer = joblib.load("model/vectorizer.pkl")
model = joblib.load("model/log_reg.pkl")   # using logistic regression

def predict_sentiment(text):
    # Convert incoming text to TF-IDF
    text_tfidf = vectorizer.transform([text])

    # Predict using ML model
    prediction = model.predict(text_tfidf)[0]

    return "Positive" if prediction == 1 else "Negative"

@app.route("/", methods=["GET"])
def home():
    return "ML Sentiment API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"error": "Text is required"}), 400

        sentiment = predict_sentiment(text)

        return jsonify({"sentiment": sentiment})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
