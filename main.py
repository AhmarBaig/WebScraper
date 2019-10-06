import requests 
from bs4 import BeautifulSoup 
from googlesearch import search

searchQuery = input("What are you looking to buy? Use this search like you use Google to buy something. The more descriptive your query is, the more accurate the search results are: ")
item = search(searchQuery, tld="com", lang="en", num=10, start=0, stop=50, pause=2.0)
URLS = []

for i in item:
  URLS.append(i)

print(URLS)