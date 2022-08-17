from sqlite3 import Date
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame


class AlpacaRepository():

    def __init__(self):
        pass

    def get_all_symbols(self):
        API_KEY = "PK2ZY1D3M66Q5ZE50WIL"
        SECRET_KEY = "OvtH7NhDyCxANBKxytcwbKLz22OHwOX8QVh0a3aB"
        PAPCA_URL = "https://paper-api.alpaca.markets"

        api = tradeapi.REST(API_KEY, SECRET_KEY, PAPCA_URL)

        assets = api.list_assets()

        symbols = list(map(lambda x: x.symbol, assets))

        return symbols

    def get_candles(self, symbol: str, start_date: str, end_date: str):

        API_KEY = "PK2ZY1D3M66Q5ZE50WIL"
        SECRET_KEY = "OvtH7NhDyCxANBKxytcwbKLz22OHwOX8QVh0a3aB"
        PAPCA_URL = "https://paper-api.alpaca.markets"
    
        api = tradeapi.REST(API_KEY, SECRET_KEY, PAPCA_URL)
    
        bars = api.get_bars(symbol, TimeFrame.Day,  start_date, end_date)
    
        return bars
    