from bs4 import BeautifulSoup as bs
import requests


outfile = open('Carlinks\carlinks.txt', 'a', encoding='utf8')
pagesfile = open('PagesLinks\links.txt', 'r', encoding='utf8')

for i in pagesfile:
    url = i.strip()

    response = requests.get(url)
    print(response)
    soup = bs(response.text, 'lxml')
    links = []
    carlinks = soup.find_all('a', class_='css-xb5nz8 ewrty961')
    for item in carlinks:
        item_url = item.get('href')
        print(item_url, file=outfile)


