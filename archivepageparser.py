outfile = open('PagesLinks\\archivelinks.txt', 'w', encoding='utf8')
s = ['https://novosibirsk.drom.ru/archive/lada/all/']
for i in range(1, 100):
    link = 'https://novosibirsk.drom.ru/lada/used/all/' + 'page' + str(i) + '/'
    s.append(link)
for i in s:
    print(i, file=outfile)