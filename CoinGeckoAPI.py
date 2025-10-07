import requests
import time
from collections import deque

prices = deque(maxlen=20)

def getSolanaPrice():
    try:
        url = 'https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT'
        response = requests.get(url)
        data = response.json()
        solanaPrice = float(data["price"])
        return solanaPrice
    except Exception as e:
        print('Error: ' + str(e))
        print(data)
        return 'Unknown Price'

def movingAverage(data, n):
    if len(data) < n:
        return None
    return sum(list(data)[-n:]) / n

lastSignal = 'sell'

while True:
    price = getSolanaPrice()
    prices.append(price)

    shortMA = movingAverage(prices, 5)
    longMA = movingAverage(prices, 20)

    print(' ')
    print(str(getSolanaPrice()) + ' $')
    print('MAShort: ' + str(shortMA) + ' $')
    print('MALong: ' + str(longMA) + ' $')

    if shortMA and longMA:
        if shortMA > longMA and lastSignal != "buy":
            print(' ')
            print('BUY')
            lastSignal = 'buy'
        elif shortMA < longMA and lastSignal != "sell":
            print(' ')
            print('SELL')
            lastSignal = 'sell'
    time.sleep(5)

    