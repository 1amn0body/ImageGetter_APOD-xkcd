import requests
from bs4 import BeautifulSoup as bs
from os.path import basename
from os import path
import os

def mkconfig():
    #test if  config exists (if not create config with filepath)
    if path.exists("comicGetterConfig.txt") != True:
        outDir = input("Set comic output directory (relative / absolute): ")

        with open("comicGetterConfig.txt", "w") as f:
            f.write(outDir)

def rdconfig():
    #read config
    with open("comicGetterConfig.txt", "r") as dir:
        out = dir.readline()

    #make filepath, if not exists
    if path.exists(out) != True:
        os.mkdir(out)

    os.chdir(out)


def saveComic(theSoup):
    imgLnk = theSoup.find(id="comic").find('img')['src']
    print("Comic from https:" + imgLnk)

    with open(basename(imgLnk), "wb") as dir:
        dir.write(requests.get("https:" + imgLnk).content)


#at start of program
mkconfig()
try:
    rdconfig()
except Exception as e:
    os.remove("comicGetterConfig.txt")
    print("No valid filepath. Try again.")
    mkconfig()



#main page comic
url = "https://xkcd.com/"
html_doc = requests.get(url).text

soup = bs(html_doc, 'html.parser')

saveComic(soup)


#older comics
prevLink = soup.find('ul', {'class': ["comicNav"]}).find('a', {'rel': ["prev"]})['href']
rePrevLink = int(prevLink.replace('/', '')) #comicnumber

i = 0
while i < 2: #second value = number of old comics to download
    urls = ("https://xkcd.com/" + str(rePrevLink - i))
    html_docs = requests.get(urls).text

    soups = bs(html_docs, 'html.parser')

    saveComic(soups)

    i = i + 1
