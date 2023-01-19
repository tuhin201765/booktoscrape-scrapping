import requests
from bs4 import BeautifulSoup as bs


i = 1
while i <= 50:
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    s = requests.Session()
    res = s.get(url)
    soup = bs(res.text, 'html.parser')
    main_div = soup.find('div', {'class': 'col-sm-8 col-md-9'})
    links = main_div.findAll('h3')
    for link in links:
        linkss = 'https://books.toscrape.com/' + link.find('a').get('href')
        with open('links.txt', 'a') as file:
            file.writelines(linkss + '\n')

    i += 1


