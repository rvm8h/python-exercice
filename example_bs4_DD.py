from bs4 import BeautifulSoup
import requests


helloworld = "<p>Hello World</p>"
soup_string = BeautifulSoup(helloworld,"html.parser")
print(soup_string)


url = "https://www.barnesandnoble.com/b/barnes-noble-classics/_/N-rqv"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")
print(soup_page)

'''
with open("foo.html") as foo_file:
    bs_soup = BeautifulSoup(foo_file, "html.parser")
print(bs_soup)
'''

html_atag = """<html><body><p>Test html a tag example</p>
<a href="http://www.test.com">Home</a>
<a href="http;//www.test.com/books">Books</a>
</body>
</html>"""

soup = BeautifulSoup(html_atag, "html.parser")
atag = soup.a
print(atag)

with open("ecologicalpyramid.html") as jungle:
    soup = BeautifulSoup(jungle, "html.parser")

    atag = soup.li.string
print(atag)


def is_secondary_consumers(tag):
    return tag.has_attr("id") and tag.get("id") == "secondaryconsumers"


"""
secondary_consumer = bs_soup.find(is_secondary_consumers())
print(secondary_consumer.li.div.string)
"""

'''
# url cible
url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"

# recuperation du contenu de la cicble
req = requests.get(url)

# traitement du contenu reçu avec html.parser ici, sinon avec lxml ou html5lib si installés
bs_soup = BeautifulSoup(req.text, "html.parser")

# affichage de toutes les balises 'th' du contenu
for th in bs_soup.find_all('th'):
    print(bs_soup.th)
    # print(bs_soup.th.string)
'''