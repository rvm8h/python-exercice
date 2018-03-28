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

secondaryconsumers = soup.find(is_secondary_consumers)
print(secondaryconsumers)
#print(secondary_consumer.li)
#print(secondary_consumer.li.div.string)

all_tertiaryconsumers = soup.find_all(class_="tertiaryconsumerlist")
print(type(all_tertiaryconsumers))
print(all_tertiaryconsumers)

all_texts = soup.find_all(text=True)
print(all_texts)

all_texts_in_list = soup.find_all(text=["plants","algae"])
print(all_texts_in_list)

div_li_tags = soup.find_all(["div", "li"])
#print(div_li_tags)

all_css_class = soup.find_all(class_=["producerlist", "primaryconsumerlist"])
#print(all_css_class)

div_li_tags = soup.find_all(["div", "li"], recursive=True)
#print(div_li_tags)

email_id_example = """<br/>
<div>The below HTML has the information that has email ids.</div>
abc@example.com
<div>xyz@example.com</div>
<span>foo@example.com</span>
 """
soup = BeautifulSoup(email_id_example, "html.parser")
emailid_regexp = re.compile("\w+@\w+\.\w+")
first_email_id = soup.find(text=emailid_regexp)
print(first_email_id)

email_ids = soup.find_all(text=emailid_regexp)
print(email_ids)

email_ids_limited = soup.find_all(text=emailid_regexp, limit=2)
print(email_ids_limited)

html_identical = """<p class="identical">
Example of p tag with class identical
</p>
<div class="identical">
Example of div tag with class identical
</div>"""
soup = BeautifulSoup(html_identical, "html.parser")
identical_div = soup.find("div", class_="identical")
print(identical_div)

