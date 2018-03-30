"""
url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
Dans ce site web travailler avec les tags th et tr pour retourner tous les noms
des stations de metros et son numero de ligne associe.
choisir son format de donnees
"""

from bs4 import BeautifulSoup
import requests


# url cible
url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"

# recuperation du contenu de la cible
rqt = requests.get(url)

# traitement du contenu reçu avec html.parser ici, sinon avec lxml ou html5lib si installé
bs_soup = BeautifulSoup(rqt.text, "html.parser")

# affichage de toutes les balises 'th' du contenu
metros = bs_soup.td.discendants

for metro in bs_soup.find_all(["tr", "td", "a"], recursive=True):
    if metro.name == 'a':
        print(metro.string)


############
'''
for th in bs_soup.find_all("th", recursive=True):
    print(bs_soup.th, '\n\n')
    print(bs_soup.th.string, '\n\n')

# affichage de toutes les balises 'tr' du contenu
for tr in bs_soup.find_all('tr'):
    print(bs_soup.tr, '\n\n')
    print(bs_soup.tr.string, '\n\n')
'''