import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from date_scrape import *
from scraping import *
from graphing import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(10,10,300,300)

        month, day, year = data_scrape("http://www.brooksbaseball.net/pfxVB/pfx.php")

        # Widget
        self.title = QLabel("Umpire Rater")
        self.grid.addWidget(self.title, 1, 1, 1, 1)
        self.title.setObjectName("title")

        self.description = QLabel("Select a date and game to see called strikes and balls plus the umpires accuracy")
        self.grid.addWidget(self.description, 2, 1, 1, 1)
        self.description.setObjectName("descript")

        self.month = QComboBox(self)
        self.grid.addWidget(self.month, 3, 1, 1, 2)
        self.monthname = [x[1] for x in month]
        self.monthnumber = [x[0] for x in month]
        self.month.addItems(self.monthname)

        self.day = QComboBox(self)
        self.grid.addWidget(self.day, 3, 3, 1, 1)
        self.day.addItems(day)

        self.year = QComboBox(self)
        self.grid.addWidget(self.year, 3, 4, 1, 1)
        self.year.addItems(year)

        self.date_button = QPushButton("Select Date")
        self.grid.addWidget(self.date_button, 3, 5, 1, 1)

        self.image = QLabel("")
        self.grid.addWidget(self.image, 1, 4, 1, 1)

        pixmap = QPixmap('mlb_logo-1.png')
        pixmap = pixmap.scaledToWidth(280)
        self.image.setPixmap(pixmap)




        # Singals/Slots
        self.date_button.clicked.connect(lambda: self.game_list())


        # Set Style
        self.set_style()


        # Draw
        self.show()

    def set_style(self):
        style_sheet = "appstyle.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())

    def game_list(self):

        day_num = self.day.currentText()
        months = self.month.currentText()

        month_num = self.monthnumber[self.monthname.index(months)]

        year_num = self.year.currentText()

        url = "http://www.brooksbaseball.net/pfxVB/pfx.php?" + "month=" + month_num + "&day=" + day_num + "&year=" + year_num

        page = requests.get(url)

        soup1 = BeautifulSoup(page.text, "html.parser")

        select = soup1.find("select", attrs={"name": "game"})

        games = select.findAll()

        gamelist = []

        for game in games:
            numbers = game['value']
            text = game.text
            gamelist.append([numbers, text])


        self.game = QComboBox(self)
        self.grid.addWidget(self.game, 4, 1, 1, 1)
        self.gamename = [x[1] for x in gamelist]
        self.gamenumber = [x[0] for x in gamelist]
        self.game.addItems(self.gamename)

        self.games_select = QPushButton("Select Game")
        self.grid.addWidget(self.games_select, 4, 2, 1, 2)



        self.games_select.clicked.connect(lambda: self.pitch_chart(url, self.game.currentText(), day_num, month_num, year_num))

        #print(gamelist)
        #return(gamelist)

    def pitch_chart(self,url, text, day, month, year):

        year_num = year
        day_num = day
        month_num = month
        game = text
        game_url = self.gamenumber[self.gamename.index(game)]


        final_url = url + "&game=" + game_url[:-1] + "%2F&prevGame=" + game_url[:-1] + "%2F&prevDate=" + month + day + "&league=mlb"

        # url = "http://www.brooksbaseball.net/pfxVB/pfx.php?" + "month=" + month + "&day=" + day + "&year=" + year + "&game=" + gametext[:-1] + "1%2F&prevDate=" + month + day + "&league=mlb"

        print(final_url)

        scraping = scrape(final_url, game_url, day_num, month_num, year_num)
        print(scraping)

        player = []

        for i in range(len(scraping) - 1):
            player.append(scraping[i + 1])

        graph(player)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())