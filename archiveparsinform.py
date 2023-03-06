from urllib import response
from bs4 import BeautifulSoup as bs
from csv import writer
import requests
import numpy as np
import pandas as pd


url = 'https://novosibirsk.drom.ru/lada/2106/48569789.html'


response = requests.get(url, timeout=5)
print(response)
keys = []
soup = bs(response.text, 'lxml')

characteristics = soup.find_all(class_='css-11ylakv ezjvm5n0')
for i in characteristics:
    item = i.find('th', class_="css-38heja ezjvm5n2")
    keys.append(item.text)


# with open('CarsInform\\archivecars.csv', 'a', newline='') as f_object:
#     writer_object = writer(f_object)
#     writer_object.writerow(['Марка', 'Модель', 'Год выпуска', 'Двигатель', 'Мощность', 'КПП', 'Привод',
#         'Цвет', 'Пробег', 'Руль', 'Поколение', 'Комплектация', 'Цена'])  
#     f_object.close()


file = open('Carlinks\\archivecarlinks.txt', 'r', encoding='utf8')
for i in file:
    url = i.strip()
    response = requests.get(url, timeout=5)
    print(response)
    soup = bs(response.text, 'lxml')

    carinfo = soup.find('h1').text
    carinfo = carinfo.split(',')
    carinfo1 = carinfo[0].split()
    carinfo2 = carinfo[1].split()
    carmark = carinfo1[1]
    carmodel = ' '.join(carinfo1[2:])
    caryear = carinfo2[0]

    s = dict()
    knowledge = soup.find_all(class_="css-11ylakv ezjvm5n0")
    for i in knowledge:
        character = i.find('th').text
        item = i.find('td').text
        if character in keys:
            s[character] = item

    spisochka = []
    for i in range(len(keys)):
        if keys[i] in s.keys():
            spisochka.append(keys[i])
        else:
            spisochka.append(0)

    stroka = [carmark, carmodel, caryear]
    for i in spisochka:
        if i in s.keys():
            stroka.append(s[i])
        else:
            stroka.append(0)

    price = soup.find(class_='css-eazmxc e162wx9x0').text
    price = price.split()
    price = ''.join(price)
    price = price.replace('₽', '')

    stroka.append(price)


    with open('CarsInform\\archivecars.csv', 'a', newline='', encoding='utf8') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(stroka)  
        f_object.close()
