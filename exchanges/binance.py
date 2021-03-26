from exchanges.config import Keys
import requests



class Binance:

    api_key = Keys.BINANCE_API_KEY
    secret_key = Keys.BINANCE_SECRET_KEY

    def get_price():
        data =  {"symbol": "BTCUSDT"}
        resp = requests.get('https://api.binance.com/api/v3/ticker/price',data)

        if resp.status_code != 200:
            return "Error "+ str(resp.status_code) 
        return int(float(resp.json()["price"]))