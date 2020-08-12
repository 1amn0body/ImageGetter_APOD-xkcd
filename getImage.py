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

#########
#get 2 older comics
prevLink = soup.find('ul', {'class': ["comicNav"]}).find('a', {'rel': ["prev"]})['href']
rePrevLink = int(prevLink.replace('/', ''))


#soup2
url2 = ("https://xkcd.com/" + str(rePrevLink))
html_doc2 = requests.get(url2).text

soup2 = bs(html_doc2, 'html.parser')

saveComic(soup2)

#soup3
url3 = ("https://xkcd.com/" + str(rePrevLink - 1))
html_doc3 = requests.get(url3).text

soup3 = bs(html_doc3, 'html.parser')

saveComic(soup3)
