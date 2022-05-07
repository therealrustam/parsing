import requests #сделать запросы к сайтам
from bs4 import BeautifulSoup


url = "https://the-flow.ru/"
cian = requests.get(url)
ciansoup = BeautifulSoup(cian.content, "html.parser")
housesFull = ciansoup.findAll(class_ = "publication__item")
for house in housesFull:
  name = house.find(class_="publication__item-title")
  price = house.find(class_="publication__item-text")
  print(f"{name} {price}")