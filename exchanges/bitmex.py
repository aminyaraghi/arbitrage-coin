from exchanges.config import Keys
import requests



class Bitmex:

    api_key = Keys.BITMEX_API_KEY
    secret_key = Keys.BITMEX_SECRET_KEY

    def get_price():
        data =  {"symbol": "XBTUSD" , "count":"1" , "reverse":"true"}
        resp = requests.get('https://www.bitmex.com/api/v1/trade',data)

        if resp.status_code != 200:
            return "Error"
        return resp.json()[0]['price']