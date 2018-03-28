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



url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")
for soup_line in soup_page.findAll('th'):
    print(soup_line.string)

