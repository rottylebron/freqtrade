# alpha_vantage_api.py
from config import ALPHA_VANTAGE_API_KEY
import requests
import pandas as pd
import time


# URL base di Alpha Vantage
BASE_URL = "https://www.alphavantage.co/query"

def get_stock_data(symbol: str, interval: str = "5min"):
    """Recupera i dati storici di un'azione da Alpha Vantage"""
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": ALPHA_VANTAGE_API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "Time Series" not in data:
        print("Errore nel recupero dati:", data)
        return None

    df = pd.DataFrame.from_dict(data[f"Time Series ({interval})"], orient="index")
    df = df.astype(float)  # Convertiamo i valori in numeri
    df.index = pd.to_datetime(df.index)  # Convertiamo l'indice in formato data
    return df

# Test della connessione
if __name__ == "__main__":
    symbol = "AAPL"  # Apple
    data = get_stock_data(symbol)
    if data is not None:
        print(data.head())  # Stampiamo le prime righe
