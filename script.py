from bs4 import BeautifulSoup
import requests
import csv 

# Setup the file
csvfile = open('anime.csv','w+')


names = []
ranks = []
description = []
up_votes = []
down_votes = []

res = requests.get('https://www.ranker.com/crowdranked-list/best-anime-series-all-time')

soup = BeautifulSoup(res.text,'html.parser')

name_list = soup.find_all('a', {'class':'listItem__title listItem__title--link black'})
for name in name_list:
    names.append(name.getText())

description_list = soup.find_all('span', {'class':'listItem__wiki block'})
for dsc in description_list:
    description.append(dsc.getText())

rank_list = soup.find_all('strong', {'class':'listItem__rank block center instapaper_ignore'})
for rank in rank_list:
    ranks.append(rank.getText())

up_votes_nodes = soup.find_all('div',{'class':'listItem__vote instapaper_ignore'})
for node in up_votes_nodes[:-1]:
    votes = node.getText().split(' ')
    up_votes.append(votes[8])
    down_votes.append(votes[10])

try:
    writer =  csv.writer(csvfile)
    writer.writerow(('Rank','Anime','Description','Up-Votes','Down-Votes'))
    for i in range(50):
        writer.writerow((ranks[i],names[i],description[i],up_votes[i],down_votes[i]))
finally:
    csvfile.close()