#url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
#Dans ce site web travailler avec les tags th et tr pour retourner tous les noms des stations de metros et le numero de lignes associe,
#choisir son format de donnees

from bs4 import BeautifulSoup
import requests


url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"

response = requests.get(url)
print(response.encoding)
soup_page = BeautifulSoup(response.content,"html.parser")
#print(soup_page)
search_lines = soup_page.find_all(["table","tb","a"])
#print(search_lines)

boolean = False

for v in search_lines:

    if  v.get("class") != None and "wikitable" in v.get("class"):
        boolean = True

    if v.has_attr("title") and "(Paris Métro)" in v.get("title") and boolean:
        print("\nMetro:",v.string)

    if v.has_attr('title') and "Paris Métro Line" in v.get("title") and v.string != None:
        print("Line: ",v.string)

