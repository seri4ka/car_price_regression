# CarPriceRegression
This project consists of collecting data and building a regression of used car prices.

1) First of all, you need to run a program to collect links to pages with cars.
This is implemented in two different files: dromparslinks.py and archive page parser.py .
One of them collects pages with cars for sale, the second with archival ones.

2) Then we collect links directly to the car cards.
This is also implemented using two files: dromparser.py and archiveparser.py .
One of them collects cards of cars for sale, the second with sold ones.

3) After that, it is necessary to collect information about cars directly.
This is still implemented by two files: dromparsinform.py and archiveparsinform.py .
One of them collects information about the cars being sold, the second about the sold ones.

4) Next, we need to run a file from the CarsInform directory, called datacleaner.ipynb.
It cleans up the data and brings it to a convenient format for further work with it

5) Finally, we can open the DromResearch.ipynb file, in which
various regressions are built directly, where information about
archived cars, and as a test - about cars sold now.


Этот проект состоит из сбора данных и построения регрессии цен на подержанные автомобили.

1)  Прежде всего вам необходимо запустить программу для сбора ссылок на страницы с автомобилями.
Это реализовано в двух разных файлах: dromparslinks.py и archive page parser.py.
Один из них собирает страницы с продающимися автомобилями, второй с архивными.

2)  Затем собираем ссылки непосредственно на карточки автомобилей.
Это также реализовано при помощи двух файлов: dromparser.py и archiveparser.py.
Один из них собирает карточки продающихся автомобилей, второй с проданными.

3) После этого необходимо собрать непосредственно информацию об автомобилях.
Это по прежнему реализовано двумя файлами: dromparsinform.py и archiveparsinform.py.
Один из них собирает информацию о продающихся автомобилях, второй о проданных.

4) Далее нам необходимо запустить файл из каталога CarsInform, под названием datacleaner.ipynb.
Он очищает данные и приводит их к удобному формату для дальнейшей работы с ним

5) Наконец мы можем открыть файл DromResearch.ipynb, в котором непосредственно происходит
построение различных регрессий, где в качестве обучающего набора выступает информация об
архивных автомобилях, а в качестве тестового - об автомобилях, продающихся сейчас.
