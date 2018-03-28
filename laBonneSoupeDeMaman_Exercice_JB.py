from bs4 import BeautifulSoup
import requests

url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"

response = requests.get(url)
soup_page = BeautifulSoup(response.content, "html.parser")

ths = soup_page.find_all('th')

for th in ths:
    th.clear()
    print(th)
