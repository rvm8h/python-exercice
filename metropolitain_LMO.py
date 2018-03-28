
#Récupération des stations de métro de Paris avec les lignes qui passent

from bs4 import BeautifulSoup
import requests

url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")
soup_table = soup_page.find('table')
for soup_line in soup_table.findAll('tr'):
    indice = 0
    for soup_case in soup_line.findAll('td'):
        for soup_station in soup_case.findAll('a'):
            if((indice == 0 or indice ==3) and not soup_station.string == None):
                print(soup_station.string)
indice+=1

