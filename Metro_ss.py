from bs4 import BeautifulSoup
import requests

url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
response = requests.get(url)
soup_page = BeautifulSoup(response.content, "html parser")
the = soup_page.find_all('th')
tre = soup_page.find_all('tr')

for line in the:
   line = soup_page.find_all(the=['station', 'numero'])
   print(line)

for line in tre:
    line = soup_page.find_all(tre=['station', 'numero'])
    print(line)


# Trouver tous les tag th dans le site web
# url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
# Dans ce site web travailler avec les tags th et tr pour retourner tous les noms des stations de metros et son numero de ligne associe.
# choisir son format de donnees
