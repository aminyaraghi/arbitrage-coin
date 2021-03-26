from exchanges.config import Keys
import requests



class CoinGecko:

    api_key = Keys.COINGECKO_API_KEY
    secret_key = Keys.COINGECKO_SECRET_KEY

    def get_price():
        data =  {"ids": "bitcoin" , "vs_currencies":"usd"}
        resp = requests.get("https://api.coingecko.com/api/v3/simple/price",data)

        if resp.status_code != 200:
            return "Error"
        return float(resp.json()["bitcoin"]["usd"])