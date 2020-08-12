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
    
#get 2 older comics
prevLink = soup.find('ul' class="comicNav").find('a' rel="prev")['href']
rePrevLink = int(prevLink.replace('/', ''))


#soup2
url2 = ("https://xkcd.com/" + rePrevLink)
html_doc2 = requests.get(url2).text

soup2 = bs(html_doc2, 'html.parser')

imgLink2 = soup2.find(id="comic").find('img')['src']

with open(basename(imgLink2), "wb") as dir:
    dir.write(requests.get("http:" + imgLink2).content)

#soup3
url3 = ("https://xkcd.com/" + (rePrevLink - 1))
html_doc3 = requests.get(url3).text

soup3 = bs(html_doc3, 'html.parser')

imgLink3 = soup3.find(id="comic").find('img')['src']

with open(basename(imgLink2), "wb") as dir:
    dir.write(requests.get("http:" + imgLink2).content)
