from bs4 import BeautifulSoup
import requests
import urllib3

url = 'http://www.aston.com'
#--------------  premier solution de connexion
http = urllib3.PoolManager()
response = http.request('GET', url)
soup_aston = BeautifulSoup(response.data.decode('utf-8'), "html.parser")
print(soup_aston)

#------------- seconde la plus utilisee
url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")
print(soup_page)

tag_th = soup_page.findAll('th')
print(tag_th)










