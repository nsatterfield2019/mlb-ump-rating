from bs4 import BeautifulSoup
import requests

url = "http://www.brooksbaseball.net/pfxVB/pfx.php"

#"http://www.brooksbaseball.net/pfxVB/pfx.php?month=5&day=9&year=2018&game=gid_2018_05_09_miamlb_chnmlb_1%2F&pitchSel=500779&prevGame=gid_2018_05_09_miamlb_chnmlb_1%2F&prevDate=59&league=mlb"

page = requests.get(url)

soup1 = BeautifulSoup(page.text, "html.parser")

select = soup1.find("select", attrs={"name": "month"})

month = select.findAll()

month_numbers = []
day_numbers = []
year_numbers = []
data = []



for months in month:
    numbers = months['value']
    text = months.text
    month_numbers.append([numbers, text])

print(month_numbers)

day_select = soup1.find("select", attrs={"name": "day"})

day = day_select.findAll()

for days in day:
    numbers = days['value']
    day_numbers.append(numbers)

print(day_numbers)

year_select = soup1.find("select", attrs={"name": "year"})

year = year_select.findAll()

for years in year:
    numbers = years['value']
    year_numbers.append(numbers)

print(year_numbers)

'''
for i in range(len(pitchers_numbers)):
    url = "http://www.brooksbaseball.net/pfxVB/pfx.php?month=5&day=9&year=2018&game=gid_2018_05_09_miamlb_chnmlb_1%2F&pitchSel=" + pitchers_numbers[i] + "&prevGame=gid_2018_05_09_miamlb_chnmlb_1%2F&prevDate=59&league=mlb"
    #print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.findAll("p")
    link = table[0].find('a')
    pitch_data = "https://www.brooksbaseball.net/pfxVB/" + link['href']
    print(pitch_data)

'''