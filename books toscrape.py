import requests
from bs4 import BeautifulSoup as bs

i = 1
url = f'https://books.toscrape.com/catalogue/page-{i}.html'
s = requests.Session()
res = s.get(url)
soup = bs(res.text, 'html.parser')
main_div = soup.find('div', {'class' : 'col-sm-8 col-md-9'})


single_link = main_div.find('h3')
print(single_link.find('a').get('href'))


links = main_div.findAll('a')
linkss = []
for link in links:
    linkss.append('https://books.toscrape.com/' + link.get('href'))
linkss.pop()
print(linkss)

