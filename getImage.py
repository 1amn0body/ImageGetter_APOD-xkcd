import requests
from bs4 import BeautifulSoup as bs

url = "https://xkcd.com/"
html_doc = requests.get(url).text

soup = bs(html_doc, 'html.parser')

print(soup.find(id="comic").find('img')['src'])

#print(soup.prettify())
