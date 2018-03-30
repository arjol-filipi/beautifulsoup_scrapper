from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
uCLient = uReq(my_url)
page_html = (uCLient.read())
uCLient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "item-container"})
brands = []
titles = []
for container in containers:
    brand = container.div.div.a.img["title"]
    brands.append(brand)
    title_container = container.findAll("a",{"class":"item-title"})
    title = title_container[0].text
    titles.append(title)
print(brands,titles)