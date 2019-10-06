# Imports
import requests 
from bs4 import BeautifulSoup 
from googlesearch import search
import json

# Input to website
searchQuery = "phones" #input("What are you looking to buy? Use this search like you use Google to buy something. The more descriptive your query is, the more accurate the search results are: ")

# Web session to store info and cookies
session = requests.Session()
idcookie = ""
item = search(searchQuery, tld="com", lang="en", num=1, start=0, stop=1, pause=2.0)

for i in item:
  session.get(i)

cookie = session.cookies.get_dict()

for i in cookie.values():
  idcookie += i

jar = requests.cookies.RequestsCookieJar()
jar.set('session', idcookie)
session.cookies = jar

# Using BeautifulSoup and requests to perform web scraping
url = 'https://www.walmart.com/search/?cat_id=0&query=' + searchQuery 
page = requests.get(url)
soup = BeautifulSoup(page.content, "html5lib")  

# Parsing the Data; links and prices
links = soup.find_all('div', attrs={'class': 'search-result-product-title gridview'})
prices = soup.find_all('span', attrs={'class': 'price-main-block'})

# Variables to properly format the Data
counter = 0
temp = ""
priceString = ""
priceList = []
formattedLinks = []
linksList = []

dictWebsiteToPrice = {}

for link in links:
  element = link.select("a[href]")
  for ttl in link:
    if str(ttl) != '<span class="visuallyhidden">Product Title</span>':
      formattedLinks.append(str(ttl)[59:])

for price in prices:
  for prc in price:
    for p in prc:
      if "visuallyhidden" in str(p):
        temp = str(p)[29:]
        temp = temp[::-1]
        temp = temp[7:]
        temp = temp[::-1]
        priceList.append(temp)

temp = ""

for i in formattedLinks:
  for j in i:
    if j != " ":
      temp += j
    else:
      linksList.append(temp)
      temp = ""
      break

print(linksList[0])

for i in range(len(linksList)):
  dictWebsiteToPrice[linksList[i].strip('"')] = priceList[i].strip("$")
  print("Item {}:\n- www.walmart.com/{}\n- Price = {}".format(i + 1, linksList[i].strip('"'), priceList[i]))

#print(dictWebsiteToPrice)