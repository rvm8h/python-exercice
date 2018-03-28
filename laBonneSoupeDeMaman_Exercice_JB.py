# Dans ce site web travailler avec les tags th et tr pour retourner tous les noms des stations de metros et son numero de ligne associe.
# choisir son format de donnees

from bs4 import BeautifulSoup
import requests
import re

url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"

response = requests.get(url)
soup_page = BeautifulSoup(response.content, "html.parser")

#print(soup_page)
pages = soup_page.find_all(['th', 'tr'])

for page in pages:
	station = ''
	number = 0
	metro = page.find(title=re.compile("(Paris Métro)"), href=re.compile("_\(Paris_M%C3%A9tro\)"))
	line = page.find(title=re.compile("Paris Métro Line"), href=re.compile("/Paris_M%C3%A9tro_Line"))
	if metro != None and line != None:
		station = metro.contents[0]
		number = line.contents[0]
		print("station: {}, Line: {}".format(station, number))
