from bs4 import BeautifulSoup
import requests
import time

url = 'https://coinmarketcap.com/de/currencies/solana/'

def getSolanaPrice():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find('span', class_='sc-65e7f566-0 WXGwg base-text')
    solanaPrice = price.get_text(strip=True)
    print(solanaPrice)

while True:
    getSolanaPrice()
    time.sleep(5)