from bs4 import BeautifulSoup
import requests


url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")
#print(soup_page)


strkey=soup_page.find_all("tr")
for st in strkey:
    #print(st)
    tag=st.findChildren(text=True)
    #print(tag)
    if "Wagram" in tag[1]:
        print(tag[1],tag[6])
        break
    elif tag[6] == '\n':
        print(tag[1],tag[7])
    else:
        print(tag[1],tag[6])
