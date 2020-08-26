import requests
from bs4 import BeautifulSoup as bs
from os.path import basename

def saveComic(theSoup):
    imgLnk = theSoup.find('img')['src']
    print("Astronomy picture of the day from https://apod.nasa.gov/" + imgLnk)

    with open(basename(imgLnk), "wb") as dir:
        dir.write(requests.get("https://apod.nasa.gov/" + imgLnk).content)

#print(soup.prettify()) #print whole html document prettified

#comic on main page (newest)
url = "https://apod.nasa.gov/"
html_doc = requests.get(url).text

soup = bs(html_doc, 'html.parser')

saveComic(soup)