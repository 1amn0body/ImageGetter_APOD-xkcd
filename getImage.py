import requests
from bs4 import BeautifulSoup as bs
from os.path import basename
from os import mkdir

url = "https://xkcd.com/"
html_doc = requests.get(url).text

soup = bs(html_doc, 'html.parser')

#print(soup.prettify()) #print whole html document prettified

imgLink = soup.find(id="comic").find('img')['src']
#print(imgLink)

with open(basename(imgLink), "wb") as dir:
    dir.write(requests.get("http:" + imgLink).content)
