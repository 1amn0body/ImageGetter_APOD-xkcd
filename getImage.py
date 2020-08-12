import requests
from bs4 import BeautifulSoup as bs
from os.path import basename
from os import mkdir

def saveComic(theSoup):
    imgLnk = theSoup.find(id="comic").find('img')['src']
    print("Comic from https:" + imgLnk)

    with open(basename(imgLnk), "wb") as dir:
        dir.write(requests.get("https:" + imgLnk).content)

#print(soup.prettify()) #print whole html document prettified

url = "https://xkcd.com/"
html_doc = requests.get(url).text

soup = bs(html_doc, 'html.parser')

saveComic(soup)

#get older comics
prevLink = soup.find('ul', {'class': ["comicNav"]}).find('a', {'rel': ["prev"]})['href']
rePrevLink = int(prevLink.replace('/', ''))

i = 0
while i < 2: #second value = number of old comics more
    urls = ("https://xkcd.com/" + str(rePrevLink - i))
    html_docs = requests.get(urls).text

    soups = bs(html_docs, 'html.parser')

    saveComic(soups)

    i = i + 1
