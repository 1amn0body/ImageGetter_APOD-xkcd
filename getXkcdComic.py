import requests
from bs4 import BeautifulSoup as bs
from os.path import basename, sep

def saveComic(theSoup, path):
    imgLnk = theSoup.find(id="comic").find('img')['src']
    print("Comic from https:" + imgLnk)

    with open(path + sep + basename(imgLnk), "wb") as dir:
        dir.write(requests.get("https:" + imgLnk).content)

    try:
        return(basename(imgLnk))
    except Exception as e:
        return('')

#print(soup.prettify()) #print whole html document prettified

def runGetter(path, max):
    dl_images = []
    if max > 0:
        #comic on main page (newest)
        url = "https://xkcd.com/"
        html_doc = requests.get(url).text

        soup = bs(html_doc, 'html.parser')

        dl_images.append(saveComic(soup, path))

        #older comics
        prevLink = soup.find('ul', {'class': ["comicNav"]}).find('a', {'rel': ["prev"]})['href']
        rePrevLink = int(prevLink.replace('/', '')) #comicnumber

        i = 0
        while i < max - 1: #second value = number of old comics to download
            urls = ("https://xkcd.com/" + str(rePrevLink - i))
            html_docs = requests.get(urls).text

            soups = bs(html_docs, 'html.parser')

            dl_images.append(saveComic(soups, path))

            i += 1
    return dl_images
