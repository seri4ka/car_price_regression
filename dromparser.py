from bs4 import BeautifulSoup as bs
import requests


pagesfile = open('PagesLinks\links.txt', 'r', encoding='utf8')

for i in pagesfile:
    url = i.strip()

    response = requests.get(url)
    print(response)
    soup = bs(response.text, 'lxml')
    links = []
    carlinks = soup.find_all('a', class_='css-xb5nz8 ewrty961')
    for item in carlinks:
        if item.find(class_="css-z5srlr e162wx9x0") == None:
            outfile = open('Carlinks\\carlinks.txt', 'a', encoding='utf8')
            item_url = item.get('href')
            print(item_url, file=outfile)
            outfile.close()
        else:
            outfile = open('Carlinks\\archivecarlinks.txt', 'a', encoding='utf8')
            item_url = item.get('href')
            print(item_url, file=outfile)
            outfile.close()

