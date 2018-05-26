from graphing import *
from scraping import *


test2 = scrape("http://www.brooksbaseball.net/pfxVB/pfx.php?month=5&day=9&year=2018&game=gid_2018_05_09_miamlb_chnmlb_1%2F&pitchSel=500779&prevGame=gid_2018_05_09_miamlb_chnmlb_1%2F&prevDate=59&league=mlb")
player = []

for i in range(len(test2) - 1):
    player.append(test2[i + 1])

graph(player)

#graph([['Ball', 1.5, 1.5]])
