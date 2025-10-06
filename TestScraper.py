from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/'
page = requests.get(url)
page_status = page.status_code
print(page_status)
html_file = BeautifulSoup(page.text, 'html')
print(html_file)