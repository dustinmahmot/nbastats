
from bs4 import BeautifulSoup
import requests

from pandas import DataFrame
import pandas

# annoying - bballref counts players who've changed teams
#           as multiple players.
#
#           so you get Nic Batum - Tot - stats
#                      Nic Batum - LAC - stats
#                      Nic Batum - PHI - stats
#
#           percentage stats won't be easily combined.

def scrape():
    resp = requests.get('https://www.basketball-reference.com/leagues/NBA_2024_totals.html')
    return resp.text


# with open('html_bballref.txt', 'w') as f:
#     f.write(scrape())
#     f.close()

html_text = ''
with open('html_bballref.txt', 'r') as f:
    html_text = f.read()
    f.close()


soup = BeautifulSoup(html_text, 'html.parser')

table = soup.find('table')

header = table.find('thead')
body = table.find('tbody')

# omits Rank and Name categories
categories = []
for cat in header.find_all('th')[2:]:
    categories.append(cat.text)

names = []
data = []
pnum = 0
for row in body.find_all('tr'):
    statnum = 0

    datarow = row.find_all('td')
    if len(datarow)==0:
        continue
    else:
        data.append([])
        for d in row.find_all('td'):
            if statnum==0:
                names.append(d.text)
            else:
                data[pnum].append(d.text)
            statnum+=1
    pnum+=1



# with open('playernames.txt','w') as f:
#     for n in names:
#         f.write(n + '\n')


# with open('playerdata.txt','w') as f:
#     for l in data:
#         for d in l:
#             f.write(d + ', ')
#         f.write('\n')
