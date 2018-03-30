from bs4 import BeautifulSoup
import requests


helloworld = "<p>Hello World</p>"
soup_string = BeautifulSoup(helloworld, "html.parser")
print(soup_string)

#on récupère le contenu d'une page que l'on parse
url = "https://www.barnesandnoble.com/b/barnes-noble-classics/_/N-rqv"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")
#print(soup_page)

#with open("foo.html") as foo_file:
#	bs_soup = BeautifulSoup(foo_file, "html.parser")
#print(bs_soup)


html_atag = """<html><body><p>Test html a tag example</p>
<a href="http://www.test.com">Home</a>
<a href="http;//www.test.com/books">Books</a>
</body>
</html>"""
soup  = BeautifulSoup(html_atag,"html.parser")
atag = soup.findAll('a')

for link in atag:
	print(link.string)

print(atag)

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

producer_entries = soup.find("ul")
print("entries: ",producer_entries.li.div.string)

t = soup.findAll("ul")
for v in t:
    print(v.li.div.string)

tag_li = soup.find("li")
print(type(tag_li))
search = soup.find(text = 'fox')
print(search)

css_class = soup.find(attrs={'class': "primaryconsumerlist"})
print("CSS :",css_class)

def is_secondary_consumers(tag):
    return tag.has_attr("id") and tag.get("id") == "secondaryconsumers"

secondary_consumers = soup.find(is_secondary_consumers)
print("test \n",secondary_consumers)


for v in secondary_consumers.find_all('div'):
    print("V:",v)
    if v != "" : print("Secondary consumers: ",v.string)