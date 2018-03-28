
#Récupération des stations de métro de Paris avec les lignes qui passent

from bs4 import BeautifulSoup
import requests

stationslist= []
lineslistlist= []
url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")
soup_table = soup_page.find('table')
for soup_line in soup_table.findAll('tr'):
    indice = 0
    station= ""
    lineslist= []
    for soup_case in soup_line.findAll('td'):
        for soup_station in soup_case.findAll('a'):
            if(indice == 0):
                station = soup_station.string
            if(indice ==3):
                lineslist.append(soup_station.string)
        indice += 1
    if not station == "":
        stationslist.append(station)
        lineslistlist.append(lineslist)
dic=dict(zip(stationslist, lineslistlist))

print(dic)
