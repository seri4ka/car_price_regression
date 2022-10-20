from bs4 import BeautifulSoup as bs
import requests


outfile = open('Carlinks\\archivecarlinks.txt', 'a', encoding='utf8')
pagesfile = open('PagesLinks\\archivelinks.txt', 'r', encoding='utf8')

for i in pagesfile:
    url = i.strip()

    response = requests.get(url)
    print(response)
    soup = bs(response.text, 'lxml')
    links = []
    carlinks = soup.find_all('a', class_='css-xb5nz8 ewrty961')
    for item in carlinks:
        if item.find(class_="css-z5srlr e162wx9x0") == None:
            continue
        else:
            item_url = item.get('href')
            print(item_url, file=outfile)

