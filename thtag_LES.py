# Trouver tout les tag th dans le site web
# url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"

from bs4 import BeautifulSoup
import requests

url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")

print(soup_page)

thtags = soup_page.findAll('th')

for t in thtags:
    print(t.string)

print("---------------------------------- TH TAGS ------------------------------------------")

for t in thtags:
    print(t)

