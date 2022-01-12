
from bs4 import BeautifulSoup
import requests

#--- PARSING SIMPLE HTML FILES.

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# read a document.
# print(doc.prettify())

# In order to find things inside the html, use the tags.
tag = doc.title
print(tag)
# Drop the tags.
print(tag.string)

# it will be changed in the document!
tag.string = "hello"
print(tag.string)

# it returns only the first occurence.
tag = doc.find("a")

tag = doc.find_all("a")
print(tag)
# in order to access to the nested structure:
print(tag[0])


#--- PARSING URL FILE.
# Some websites block you whenever you do scraping like these.

url = "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-gaming-z-trio-10g-lhr/p/N82E16814137677?Description=gpu&cm_re=gpu-_-14-137-677-_-Product"

result = requests.get(url)
# print(result.text)

doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())
# the price of the gpu

# find a dollar text, not a tag.
prices = doc.find_all(text = "$")
# it returns only the $ sign but not the price.
print(prices)

# parent refers to super object of the $.
print(prices[0].parent)

print(prices[0].parent.find("strong").string)













# https://www.youtube.com/watch?v=gRLHr664tXA&list=PLzMcBGfZo4-lSq2IDrA6vpZEV92AmQfJK




