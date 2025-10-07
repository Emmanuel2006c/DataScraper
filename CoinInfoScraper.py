from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.coinlore.com/de/coin/solana'

def getSolanaPrice():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find('span', id = 'hprice')
    solanaPrice = price.get_text(strip=True)
    print(solanaPrice)

while True:
    getSolanaPrice()
    time.sleep(5)