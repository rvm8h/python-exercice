#Trouver tout les tag th dans le site web
#url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
#Dans ce site web travailler avec les tags th et tr pour retourner tous les noms des stations de metros et le numero de lignes associe,
#choisir son format de donnees

from bs4 import BeautifulSoup
import requests


url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"

response = requests.get(url)
print(response.encoding)
soup_page = BeautifulSoup(response.content,"html.parser")
search_entries = soup_page.find_all("th")


#print("Search entries:\n",search_entries)

#print(search_entries.th.string)

for v in search_entries:

    print("V = ",v)
    print(v.string)


