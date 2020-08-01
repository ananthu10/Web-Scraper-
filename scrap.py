import pprint
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/front')
print(res)
res2 = requests.get('https://news.ycombinator.com/front?day=2020-06-26&p=3')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links+links2
mega_subtext = subtext+subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        print('#################')
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        print(f'title={title},href={href},vote={vote}')
        print('#################')

        if len(vote):
            points = int(vote[0].getText().split(' ')[0])
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


create_custom_hn(mega_links, mega_subtext)
