import csv

import requests
from bs4 import BeautifulSoup as bs

with open('links.txt', 'r') as file:
    urls = file.readlines()
print(urls)
for url in urls:
    url = url.strip('\n')
    s = requests.Session()
    r = s.get(url)
    soup = bs(r.text, 'html.parser')
    bn = soup.find('h1').text
    bp = soup.find('p', {'class': 'price_color'}).text
    bimage = soup.find('div', {'class': 'item active'}).find('img').get('src')
    book = {'Book name': bn, 'Book Price': bp, 'Book image': bimage}
    with open('links.csv', 'a',newline='') as file:
        writer = csv.DictWriter(file,fieldnames=book.keys())
        writer.writerow(book)

