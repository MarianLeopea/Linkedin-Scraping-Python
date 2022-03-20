import requests
from bs4 import BeautifulSoup

baseurl = "https://www.linkedin.com"

headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

r = requests.get('https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22106670623%22%5D&keywords=website&origin=FACETED_SEARCH&page=2&position=0&searchId=37bba5c9-e5a7-40be-8a8f-9632847ef30b&sid=%3Ay0')
soup = BeautifulSoup(r.content, 'lxml')

productlist = soup.find('div', class_='search-results-container')
print(productlist)
