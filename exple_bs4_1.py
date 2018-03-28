from bs4 import BeautifulSoup
import requests


helloworld = "<p>Hello World</p>"
soup_string = BeautifulSoup(helloworld, "html.parser")
print(soup_string)


url = "https://www.barnesandnoble.com/b/barnes-noble-classics/_/N-rqv"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")
print(soup_page)

with open("foo.html") as foo_file:
	soup = BeautifulSoup(foo_file, "html.parser")
print(soup)


html_atag = """<html><body><p>Test html a tag example</p>
<a href="http://www.test.com">Home</a>

</body>
</html>"""
soup  = BeautifulSoup(html_atag,"html.parser")
atag = soup.a
print(atag)


url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
response = requests.get(url)
soup_page= BeautifulSoup(response.content,"html parser")
print(soup_page)

tag_th=soup_page.find_all('th')
print(tag_th)

with open("ecologicalpyramid.html") as ecological_pyramid:
 soup = BeautifulSoup(ecological_pyramid,"html.paser")
produce_stories = soup.find_all("ul")
print(produce_stories.li.div.string)
search = soup.find_all(text="fo")
print(search)