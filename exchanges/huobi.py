from exchanges.config import Keys
import requests



class Huobi:

    api_key = Keys.HUOBI_API_KEY
    secret_key = Keys.HUOBI_SECRET_KEY

    def get_price():
        resp = requests.get('https://api.huobi.pro/market/trade?symbol=btcusdt')

        if resp.status_code != 200:
            return "Error "+ str(resp.status_code)
        return float(resp.json()["tick"]["data"][0]["price"])