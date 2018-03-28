#url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
#Dans ce site web travailler avec les tags th et tr pour retourner tous les noms des stations de metros et le numero de lignes associe,
#choisir son format de donnees

from bs4 import BeautifulSoup
import requests
import re

url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"

response = requests.get(url)
print(response.encoding)
soup_page = BeautifulSoup(response.content,"html.parser")
#print(soup_page)
regex = r"Paris Métro Line [0-9]*"

metrolineregex = re.compile(regex)
print(metrolineregex)

metroline = soup_page.find_all(text=metrolineregex)

print(metroline)

#search_station = soup_page.find_all(["tr","div", "li","a"], class_ = "mw-redirect", recursive= True)
search_lines = soup_page.find_all(["td","a"])


#print("Search entries:\n",search_lines)

#print(search_entries.th.string)

for v in search_lines:

    print("V = ",v)
    if v.string != None:
        print("Line: ",v.string)

#for v in search_station:

#    if v.string != None:
#        print("Station: ",v.string)
