from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup
import requests

url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find('table')
#print(table)

for tr in table.findAll('tr'):
    for td in tr.findAll('td')[::3]:# en sautant le deux cases et prendre le 3
        for a in td.findAll('a'):
          print(a.text)
# Trouver tous les tag th dans le site web
# url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
# Dans ce site web travailler avec les tags th et tr pour retourner tous les noms des stations de metros et son numero de ligne associe.
# choisir son format de donnees
