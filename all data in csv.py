import requests
from bs4 import BeautifulSoup as bs

url = 'https://books.toscrape.com/catalogue/worlds-elsewhere-journeys-around-shakespeares-globe_972/index.html'
book = {}
s = requests.Session()
r = s.get(url)
soup = bs(r.text, 'html.parser')
bn = soup.find('h1').text
bp = soup.find('p', {'class':'price_color'}).text
bimage = soup.find('div', {'class': 'item active'}).find('img').get('src')
book = {'Book name': bn , 'Book Price': bp, 'Book image': bimage}
print(book)