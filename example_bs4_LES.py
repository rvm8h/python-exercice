from bs4 import BeautifulSoup
import requests


helloworld = "<p>Hello World</p>"
soup_string = BeautifulSoup(helloworld, "html.parser")
print(soup_string)

url = "https://www.barnesandnoble.com/b/barnes-noble-classics/_/N-rqv"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")
print(soup_page)

html_atag = """<html><body><p>Test html a tag example</p>
<a href="http://www.test.com">Home</a>
<a href="http;//www.test.com/books">Books</a>
</body>
</html>"""
soup = BeautifulSoup(html_atag,"html.parser")
atag = soup.a
atags = soup.findAll('a')
print(atag)
print(atags[1])
print(type(atags))

for link in atags:
    print(link.string)
ptag = soup.p
print(ptag)

with open("ecologicalpyramid.html") as foo_file:
	soup = BeautifulSoup(foo_file, "html.parser")
print(soup)

print("---------- Recherche de texte brut ---------")
search = soup.find(text='fox')
print(search)

css_class = soup.find(attrs={"class":"primaryconsumerlist"})
css_class = soup.find(class_="primaryconsumerlist")
print(css_class)

def is_secondary_consumers(tag):
    #print(type(tag))
    #print(tag)
    return tag.has_attr("id") and tag.get("id") == "secondaryconsumers"

secondary_consumer = soup.find(is_secondary_consumers)
print(secondary_consumer.li)
print(secondary_consumer.li.div.string)



