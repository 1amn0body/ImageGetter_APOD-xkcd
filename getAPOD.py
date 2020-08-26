import requests
from bs4 import BeautifulSoup as bs
from os.path import basename
from datetime import date, timedelta

def saveComic(theSoup):
    x = False
    try:
        imgLnk = theSoup.find('img')['src']
        x = True
    except Exception as e:
        print("Image not found or other exception. More infos here: " + str(e))

    if x == True:
        print("Astronomy picture of the day from https://apod.nasa.gov/" + imgLnk)

        with open(basename(imgLnk), "wb") as dir:
            dir.write(requests.get("https://apod.nasa.gov/" + imgLnk).content)

#print(soup.prettify()) #print whole html document prettified

#comic on main page (newest)
url = "https://apod.nasa.gov/"
html_doc = requests.get(url).text

soup = bs(html_doc, 'html.parser')

saveComic(soup)

#older pictures
dateBeforeToday = date.today() - timedelta(days = 1)

i = 0
while i < 0: #second value = number of old comics to download
    urls = ("https://apod.nasa.gov/apod/ap" + str(dateBeforeToday.strftime("%Y%m%d")[2:]) + ".html")
    html_docs = requests.get(urls).text

    soups = bs(html_docs, 'html.parser')

    saveComic(soups)

    i = i + 1
    dateBeforeToday = date.today() - timedelta(days = i + 1)
