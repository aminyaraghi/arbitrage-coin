from flask import Flask
from flask import render_template
from exchanges.binance import Binance
from exchanges.coingecko import CoinGecko
from exchanges.nobitex import Nobitex
from exchanges.bitmex import Bitmex
from exchanges.huobi import Huobi
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getdata')
def get_data():
    data  = {
        'binance': Binance.get_price(),
        'coingecko' : CoinGecko.get_price(),
        'nobitex' : Nobitex.get_price(),
        'bitmex' : Bitmex.get_price(),
        'huobi' : Huobi.get_price()
    }
    minkey = min(data.keys(), key=(lambda k: data[k]))
    maxkey = max(data.keys(), key=(lambda k: data[k]))
    data['min'] = data[minkey]-10
    data['diff'] = data[maxkey]-data[minkey]
    data['minkey'] = minkey
    data['maxkey'] = maxkey
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

