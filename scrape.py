import urllib2
from bs4 import BeautifulSoup

with open('url.txt') as f:
    url = f.read()

page = urllib2.urlopen(url).read()

with open('oldOffers.html') as f:
        oldOffers = f.read().splitlines()

soup = BeautifulSoup(page, "lxml")

newOffers = []
for tr in soup.find_all('tr')[2:]:
    for tds in tr.find_all('td', class_="offer"):
        for offer in tds.find_all('a', href=True):
            link = offer.get('href')
            newOffers.append(link)

newOffers = filter(lambda x: len(x) > 5, newOffers)

diff = list(set(newOffers) - set(oldOffers))
print diff
