import requests
import time
from collections import deque

balance = 0
buyPrice = 0
sellPrice = 0

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
    if shortMA != None and longMA != None:
        print('MAShort: ' + str(round(shortMA, 2)) + ' $')
        print('MALong: ' + str(round(longMA, 2)) + ' $')
        print('Balance: ' + str(round(balance, 2)))
    else:
        print('Waiting for MAs to be calculated...')

    if shortMA and longMA:
        if shortMA > longMA and lastSignal != "buy":
            print(' ')
            print('BUY')
            buyPrice = getSolanaPrice()
            lastSignal = 'buy'
        elif shortMA < longMA and lastSignal != "sell":
            print(' ')
            print('SELL')
            sellPrice = getSolanaPrice()
            balance = balance + (sellPrice - buyPrice)
            lastSignal = 'sell'
    time.sleep(5)

    