from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    pair = request.args.get("pair", "BTC/USDT")
    prediction = random.uniform(-0.05, 0.05)  # Simuliamo una previsione AI
    return jsonify({"pair": pair, "prediction": prediction})

@app.route('/sentiment', methods=['GET'])
def sentiment():
    pair = request.args.get("pair", "BTC/USDT")
    sentiment_score = random.uniform(-1, 1)  # Simuliamo il sentiment
    return jsonify({"pair": pair, "sentiment_score": sentiment_score})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
