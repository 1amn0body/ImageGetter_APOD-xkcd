import requests
from bs4 import BeautifulSoup as bs
#from os.path import expanduser, exists
from os.path import basename
#from pathlib import Path

url = "https://xkcd.com/"
html_doc = requests.get(url).text

soup = bs(html_doc, 'html.parser')

#print(soup.prettify()) #print whole html document prettified

imgLink = soup.find(id="comic").find('img')['src']
print(imgLink)

#userPath = expanduser("~")
#filePath = Path("Desktop")

#print(Path.cwd()) #now active path / path of this file

#save img
#with open("Y:\\ERIK\\Informatik\\Python\\xkcdComicGetter", "wb") as dir:
#    dir.write(requests.get("http:" + imgLink).content)

with open(basename(imgLink), "wb") as dir:
    dir.write(requests.get("http:" + imgLink).content)
