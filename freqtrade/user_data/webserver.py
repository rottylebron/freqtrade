from flask import Flask, request, jsonify
import ccxt

app = Flask(__name__)

# Configurazione Binance API
exchange = ccxt.binance({
    "apiKey": "qmabmzIXz2iJGjFxyNKf3K4kolOEnP2XoBUbHpqJWA1bazAVIgUZBtdWPk7OVI97",
    "secret": "jqvdy9H0qNojP8PtJDGiujtUoRYPn6Ew7FKkbIG9TO5djBe1cEksf8TBMjbLP5xC",
    "enableRateLimit": True
})

@app.route('/manual_order', methods=['POST'])
def manual_order():
    """ API per eseguire ordini manuali dalla UI """
    data = request.json
    pair = data.get("pair")
    order_type = data.get("type", "market")
    side = data.get("side", "buy")
    amount = data.get("amount", 1)

    try:
        order = exchange.create_order(symbol=pair, type=order_type, side=side, amount=amount)
        return jsonify({"status": "success", "order": order})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/bot_status', methods=['GET'])
def bot_status():
    """ API per verificare lo stato del bot """
    return jsonify({"status": "running"})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001)
