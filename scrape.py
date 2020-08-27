import requests
from bs4 import BeautifulSoup
import pprint

n_pages = int(input("Number of pages: "))
links = []
subtext = []

def sort_by_points(hnlist):
    return sorted(hnlist, key= lambda k:k['score'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title':title, 'score':points, 'link':href})
    return sort_by_points(hn)

for page in range(1, n_pages+1):
    res = requests.get('https://news.ycombinator.com/news?p=' + str(page))
    soup = BeautifulSoup(res.text, 'html.parser')
    links += soup.select('.storylink')
    subtext += soup.select('.subtext')

pprint.pprint(create_custom_hn(links, subtext))
