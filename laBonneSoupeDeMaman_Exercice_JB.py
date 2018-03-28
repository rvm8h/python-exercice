from bs4 import BeautifulSoup
import requests
import re

url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"

response = requests.get(url)
soup_page = BeautifulSoup(response.content, "html.parser")

ths = soup_page.find_all('th')

for th in ths:
    th.clear()
    print(th)

helloworld = "<p>Hello World</p>"
soup_string = BeautifulSoup(helloworld, "html.parser")
#print(soup_string)


url = "https://www.barnesandnoble.com/b/barnes-noble-classics/_/N-rqv"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")
#print(soup_page)

#with open("foo.html") as foo_file:
#	soup = BeautifulSoup(foo_file, "html.parser")
#print(soup)


html_atag = """<html><body><p>Test html a tag example</p>
<a href="http://www.test.com">Home</a>
<a href="http;//www.test.com/books">Books</a>
</body>
</html>"""
soup  = BeautifulSoup(html_atag,"html.parser")
alltag = soup.findAll('a')
atag = soup.a
#print(atag)

html_identical = """<p class="identical">
Example of p tag with class identical
</p>
<div class="identical">
Example of div tag with class identical
</div>"""
soup = BeautifulSoup(html_identical, "html.parser")
identical_div = soup.find("div", class_="identical")
#print(identical_div)

with open("ecologicalpyramid.html") as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, "html.parser")

producer_entries = soup.find("ul")
#print(producer_entries.li.div.string)

tag_li = soup.find('li')
#print(tag_li)

search = soup.find(text='fox')
#print(search)


css_class = soup.select("[class~=primaryconsumerlist]")
css_class = soup.find(class_="primaryconsumerlist")
css_class = soup.find(attrs={"class": "primaryconsumerlist"})
css_class = soup.select(".primaryconsumerlist")
#print(css_class)

def is_secondary_consumers(tag):
    return tag.has_attr("id") and tag.get('id') == "secondaryconsumers"

secondary_consumer = soup.find(is_secondary_consumers)
#print(secondary_consumer)

all_tertiaryconsumers = soup.find_all(class_="tertiaryconsumerlist")
#print(all_tertiaryconsumers)

all_texts = soup.find_all(text=True)
#print(all_texts)

all_texts_in_list = soup.find_all(text=["plants", "algae"])
#print(all_texts_in_list)

div_li_tags = soup.find_all(["div", "li"])
#print(div_li_tags)

all_css_class = soup.select(".tertiaryconsumerlist")
#print(all_css_class)

emailid_regexp = re.compile("^b")
email_ids = soup.find_all(text=emailid_regexp)
print(email_ids)
