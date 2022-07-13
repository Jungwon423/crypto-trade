from binance.client import Client
import pandas as pd

api_key = 'GE0szCw2QcMowjVZXhKyCdnXhlkwMO6uX3njiA4nKTi6YThODfbQ268wX8J1Zrsc'
api_secret = 'Th4fDaZIOn90UUpDSW7vxoSak5bkmk8phscJc3xIOqE3XqmrVG7Oq1uKjnWD9Plt'

client = Client(api_key=api_key, api_secret=api_secret)

# 티커 조회

tickers = client.get_all_tickers()
print(type(tickers), len(tickers))

df = pd.DataFrame(data=tickers)
df.set_index('symbol', inplace=True)
df