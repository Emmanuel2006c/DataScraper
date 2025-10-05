from bs4 import BeautifulSoup
import requests

url = requests.get("https://www.coingecko.com/de")

soup = BeautifulSoup(url.text, 'html.parser')


#f = open("coingecko.html", 'r', encoding='utf-8')
#inhalt = f.read()
#zeilen = f.readlines()
#f.close()
#print(zeilen[:10])
print("Hello World")