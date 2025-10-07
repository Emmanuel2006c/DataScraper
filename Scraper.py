from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt

def getcoinpage(slug = "solana"):
    url = f"https://coinmarketcap.com/de/currencies/{slug}"
    page = requests.get(url, timeout = (3,10))
    print(page.status_code)
    page.raise_for_status()
    return page.text, url

def getliveprice(html):
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find("span", class_="sc-65e7f566-0 WXGwg base-text")
    price_text = price.get_text(strip=True)
    return price_text

df = pd.DataFrame(columns=["Datetime", "Price"])
i = 0
while i <10:
    html, url = getcoinpage("solana")
    price = getliveprice(html)
    df.loc[len(df)] = [datetime.now(), price]
    i += 1
    time.sleep(10)
print(df)
plt.plot(df["Datetime"], df["Price"])
plt.xlabel("Datetime")
plt.ylabel("Price")
plt.title("Solanapreis über Zeit")