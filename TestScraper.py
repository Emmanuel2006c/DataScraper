from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/simple/'
page = requests.get(url)
page_status = page.status_code
html_file = BeautifulSoup(page.text, 'html.parser')
header = html_file.find('title')
j = 0

print(page_status)

print(header)

for h3 in html_file.find_all('h3'):
    country = str(h3.get_text(strip=True))
    i = 0
    for span in html_file.find_all('span', class_='country-capital'):
        capital = str(span.get_text(strip=True))
        if i < j:
            i = i + 1
            continue
        print(country + ': ' + capital)
        j = j + 1
        break