from bs4 import BeautifulSoup
import requests

# finding all pitchers


def scrape(url):
#url = "http://www.brooksbaseball.net/pfxVB/pfx.php?month=5&day=9&year=2018&game=gid_2018_05_09_miamlb_chnmlb_1%2F&pitchSel=500779&prevGame=gid_2018_05_09_miamlb_chnmlb_1%2F&prevDate=59&league=mlb"

    page = requests.get(url)

    soup1 = BeautifulSoup(page.text, "html.parser")

    select = soup1.find("select", attrs={"name": "pitchSel"})

    pitchers = select.findAll()

    pitchers_numbers = []
    data = []

    for pitcher in pitchers:
        numbers = pitcher['value']
        pitchers_numbers.append(numbers)
        #print(numbers)

    for i in range(len(pitchers_numbers)):
        url = "http://www.brooksbaseball.net/pfxVB/pfx.php?month=5&day=9&year=2018&game=gid_2018_05_09_miamlb_chnmlb_1%2F&pitchSel=" + pitchers_numbers[i] + "&prevGame=gid_2018_05_09_miamlb_chnmlb_1%2F&prevDate=59&league=mlb"
        #print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        table = soup.findAll("p")
        link = table[0].find('a')
        pitch_data = "https://www.brooksbaseball.net/pfxVB/" + link['href']
        #print(pitch_data)
        data.append(pitch_data)

    all_pitches = [["pdes", "px", "pz"]]

    for i in range(len(data)):
        dataurl = data[i]
        page = requests.get(dataurl)

        soup = BeautifulSoup(page.text, "html.parser")

        pitchestable = soup.find("table")

        pitch_list = pitchestable.findAll("tr")

        pitch_list.pop(0)

        pitches = [[y.text for y in x.findAll("td")] for x in pitch_list]

        # print(pitches)

        pdes = [x[23] for x in pitches]
        px = [float(x[-6]) for x in pitches]
        pz = [float(x[-5]) for x in pitches]

        for i in range(len(pdes)):
            all_pitches.append([pdes[i], px[i], pz[i]])

    return(all_pitches)


scrape("http://www.brooksbaseball.net/pfxVB/pfx.php?month=3&day=1&year=2007&game=gid_2007_03_01_arimlb_chamlb_1/")

# http://www.brooksbaseball.net/pfxVB/pfx.php?month=5&day=9&year=2018&game=gid_2018_05_09_miamlb_chnmlb_1%2F&pitchSel=500779&prevGame=gid_2018_05_09_miamlb_chnmlb_1%2F&prevDate=59&league=mlb


# http://www.brooksbaseball.net/pfxVB/pfx.php?month=5&day=24&year=2018&game=gid_2018_05_24_balmlb_chamlb_1%2F&prevGame=gid_2018_05_29_anamlb_detmlb_1%2F&prevDate=524&league=mlb
