import ccxt
import pprint
import pandas as pd 

binance = ccxt.binance()
markets= binance.load_markets()

# 시장 조회
# print(markets.keys())
# print(len(markets))

# 현재가 조회
# binance = ccxt.binance()
# btc = binance.fetch_ticker("BTC/USDT")
# pprint.pprint(btc)

# 과거 데이터 조회 - 분봉 조회
# btc_ohlcv = binance.fetch_ohlcv("BTC/USDT")

# df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
# df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
# df.set_index('datetime', inplace=True)
# print(df)

# 과거 데이터 조회 - 일봉 조회
# btc_ohlcv = binance.fetch_ohlcv("BTC/USDT", '1d')

# df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
# df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
# df.set_index('datetime', inplace=True)
# print(df)

# 과거 데이터 조회 - 특정 개수만 조회하기
# btc_ohlcv = binance.fetch_ohlcv(symbol="BTC/USDT", timeframe='1d', limit=10)

# df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
# df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
# df.set_index('datetime', inplace=True)
# print(df)

# 호가 조회
# exchange = ccxt.binance()
# orderbook = exchange.fetch_order_book('ETH/USDT')
# print(orderbook['asks'])
# print(orderbook['bids'])

# 잔고 조회
binance = ccxt.binance(config={
    'apiKey': 'GE0szCw2QcMowjVZXhKyCdnXhlkwMO6uX3njiA4nKTi6YThODfbQ268wX8J1Zrsc',
    'secret': 'Th4fDaZIOn90UUpDSW7vxoSak5bkmk8phscJc3xIOqE3XqmrVG7Oq1uKjnWD9Plt'
})

# balance = binance.fetch_balance()
# print(balance['USDT'])

# 현물 거래 - 매수 주문
# order = binance.create_limit_buy_order(
#     symbol="BTC/USDT", 
#     amount=0.00001, 
#     price=20000
# )
# pprint.pprint(order)

# 현물 거래 - 주문 취소
# resp = binance.cancel_order(
#     id=5221422745,
#     symbol='BTC/USDT'
# )
# pprint.pprint(resp)

# 선물거래
binance = ccxt.binance(config={
    'apiKey': 'GE0szCw2QcMowjVZXhKyCdnXhlkwMO6uX3njiA4nKTi6YThODfbQ268wX8J1Zrsc',
    'secret': 'Th4fDaZIOn90UUpDSW7vxoSak5bkmk8phscJc3xIOqE3XqmrVG7Oq1uKjnWD9Plt',
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

# markets = binance.load_markets()
# for m in markets:
#     print(m)

# 선물 잔고 조회
# balance = binance.fetch_balance(params={"type": "future"})
# print(balance['USDT'])

# 현재가 조회
# btc = binance.fetch_ticker("BTC/USDT")
# print(btc)

# 과거 데이터 조회
# btc = binance.fetch_ohlcv(
#     symbol="BTC/USDT", 
#     timeframe='1d', 
#     since=None, 
#     limit=10)
# df = pd.DataFrame(btc, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
# df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
# df.set_index('datetime', inplace=True)
# print(df)

# 매수/롱 포지션 진입
# order = binance.create_market_buy_order(
#     symbol="BTC/USDT",
#     amount=0.001
# )
# pprint.pprint(order)

# 매수/롱 포지션 정리
# order = binance.create_market_sell_order(
#     symbol="BTC/USDT",
#     amount=0.001
# )
# pprint.pprint(order)

# 레버리지 설정
# markets = binance.load_markets()
# symbol = "BTC/USDT"
# market = binance.market(symbol)
# leverage = 20
# resp = binance.fapiPrivate_post_leverage({
#     'symbol': market['id'],
#     'leverage': leverage
# })
# order = binance.create_market_buy_order(
#     symbol=symbol,
#     amount=0.001,
# )

# 포지션 얻기
# balance = binance.fetch_balance()
# positions = balance['info']['positions']
# for position in positions:
#     if position["symbol"] == "BTCUSDT":
#         pprint.pprint(position)

# 대기 주문 조회
# open_orders = binance.fetch_open_orders(
#     symbol="BTC/USDT"
# )
# pprint.pprint(open_orders)

# 시장가 주문과 TP/SL
# orders = [None] * 3

# # market price (ex: 19500$)
# orders[0] = binance.create_order(
#     symbol="BTC/USDT",
#     type="MARKET",
#     side="buy",
#     amount=0.001
# )

# # take profit
# orders[1] = binance.create_order(
#     symbol="BTC/USDT",
#     type="TAKE_PROFIT_MARKET",
#     side="sell",
#     amount=0.001,
#     params={'stopPrice': 19700}
# )

# # stop loss
# orders[2] = binance.create_order(
#     symbol="BTC/USDT",
#     type="STOP_MARKET",
#     side="sell",
#     amount=0.001,
#     params={'stopPrice': 19300}
# )

# for order in orders:
#     pprint.pprint(order)

# 지정가 주문과 TP/SL
# orders = [None] * 3
# price = 19400

# # limit price
# orders[0] = binance.create_order(
#     symbol="BTC/USDT",
#     type="LIMIT",
#     side="buy",
#     amount=0.001,
#     price=price
# )

# # take profit
# orders[1] = binance.create_order(
#     symbol="BTC/USDT",
#     type="TAKE_PROFIT",
#     side="sell",
#     amount=0.001,
#     price=price,
#     params={'stopPrice': 19600}
# )

# # stop loss
# orders[2] = binance.create_order(
#     symbol="BTC/USDT",
#     type="STOP",
#     side="sell",
#     amount=0.001,
#     price=price,
#     params={'stopPrice': 19200}
# )

# for order in orders:
#     pprint.pprint(order)