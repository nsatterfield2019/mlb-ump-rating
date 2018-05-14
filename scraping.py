from bs4 import BeautifulSoup
import requests

url = "http://www.brooksbaseball.net/pfxVB/pfx.php?month=5&day=9&year=2018&game=gid_2018_05_09_miamlb_chnmlb_1%2F&pitchSel=500779&prevGame=gid_2018_05_09_miamlb_chnmlb_1%2F&prevDate=59&league=mlb"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

#scraping the data table for one pitcher, will change to all pitchers eventually
table = soup.findAll("p")

link = table[0].find('a')
data = "https://www.brooksbaseball.net/pfxVB/" + link['href']
print(data)


dataurl = data
page = requests.get(dataurl)

soup = BeautifulSoup(page.text, "html.parser")

pitches = soup.findAll("table")

print(pitches)
