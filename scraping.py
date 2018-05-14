from bs4 import BeautifulSoup
import requests

url = "http://www.brooksbaseball.net/pfxVB/pfx.php"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

