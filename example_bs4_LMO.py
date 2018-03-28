from bs4 import BeautifulSoup
import requests


helloworld = "<p>Hello World</p>"
soup_string = BeautifulSoup(helloworld, "html.parser")
print(soup_string)


url = "https://www.barnesandnoble.com/b/barnes-noble-classics/_/N-rqv"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")
#print(soup_page)

# with open("foo.html") as foo_file:
# 	soup = BeautifulSoup(foo_file, "html.parser")
# print(soup)


html_atag = """<html><body><p>Test html a tag example</p>
<a href="http://www.test.com">Home</a>
<a href="http;//www.test.com/books">Books</a>
</body>
</html>"""
soup  = BeautifulSoup(html_atag,"html.parser")
atag = soup.a
print(atag)
for atag in soup.findAll('a'):
    print(atag.string)

print(type(atag))

html_identical = """<p class="identical">
Example of p tag with class identical
</p>
<div class="identical">
Example of div tag with class identical
</div>"""
soup = BeautifulSoup(html_identical, "html.parser")
identical_div = soup.find("div", class_="identical")
print(identical_div)

with open("ecologicalpyramid.html") as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, "html.parser")
# producer_entries = soup.find("ul")
# print(producer_entries.li.div.string)
for producer_entry in soup.findAll("ul"):
    print(producer_entry.li.div.string)

search=soup.find(text='fox')
print(search)
css_class = soup.findAll(attrs={"class": "primaryconsumerlist"})
print(css_class)
#Est équivalent à (attention c'est "class_", parce que le mot "class" est réservé en Python)
css_class = soup.findAll(class_="primaryconsumerlist")
print(css_class)

def is_secondary_consumer(tag):
    return tag.has_attr("id") and tag.get("id") == "secondaryconsumers"

secondary_consumers = soup.find(is_secondary_consumer)
for producer_entry in secondary_consumers.findAll(attrs={"class": "name"}):
    print(producer_entry.string)



# url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
# response = requests.get(url)
# soup_page = BeautifulSoup(response.content,"html.parser")
# for soup_line in soup_page.findAll('th'):
#     print(soup_line.string)


