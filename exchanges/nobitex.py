from exchanges.config import Keys
import requests



class Nobitex:

    api_key = Keys.NOBITEX_API_KEY
    secret_key = Keys.NOBITEX_SECRET_KEY

    def get_price():
        data =  {"srcCurrency":"btc","dstCurrency":"usdt,rls"}
        resp = requests.post('https://api.nobitex.ir/market/stats',data)

        if resp.status_code != 200:
            return "Error"
        return int(float(resp.json()['stats']['btc-usdt']['latest']))#+'  -  RLS : '+ str(float(resp.json()['stats']['btc-rls']['latest']))