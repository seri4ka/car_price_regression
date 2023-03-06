archivelinks = open('archivecarlinks.txt', 'r', encoding='utf8')
carlinks = open('carlinks.txt', 'r', encoding='utf8')
s1 = []
s2 = []
for i in archivelinks:
    s1.append(i.strip())
for i in carlinks:
    s2.append(i.strip())
mn1 = set(s1)
mn2 = set(s2)
outfile = open('archivecarlinks.txt', 'w', encoding='utf8')
for i in mn1:
    print(i, file=outfile)
outfile.close()
outfile = open('carlinks.txt', 'w', encoding='utf8')
for i in mn2:
    print(i, file=outfile)
outfile.close()
