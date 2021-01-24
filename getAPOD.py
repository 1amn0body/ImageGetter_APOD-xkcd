import requests
from bs4 import BeautifulSoup as bs
from os.path import basename, sep
from datetime import date, timedelta

def saveComic(theSoup, path):
    x = False
    try:
        imgLnk = theSoup.find('img')['src']
        x = True
    except Exception as e:
        print("Image not found or other exception. More infos here: " + str(e))

    if x == True:
        print("Astronomy picture of the day from https://apod.nasa.gov/" + imgLnk)

        with open(path + sep + basename(imgLnk), "wb") as dir:
            dir.write(requests.get("https://apod.nasa.gov/" + imgLnk).content)

        return(basename(imgLnk))
    return('')

#print(soup.prettify()) #print whole html document prettified
def runGetter(path, max):
    dl_images = []
    if max > 0:
        #comic on main page (latest)
        url = "https://apod.nasa.gov/"
        html_doc = requests.get(url).text

        soup = bs(html_doc, 'html.parser')

        dl_images.append(saveComic(soup, path))

        #older pictures
        dateBeforeToday = date.today() - timedelta(days = 1)

        i = 0
        while i < max - 1: #second value = number of old apods to download
            urls = ("https://apod.nasa.gov/apod/ap" + str(dateBeforeToday.strftime("%Y%m%d")[2:]) + ".html")
            html_docs = requests.get(urls).text

            soups = bs(html_docs, 'html.parser')

            dl_images.append(saveComic(soups, path))

            i += 1
            dateBeforeToday = date.today() - timedelta(days = i + 1)
    return dl_images
