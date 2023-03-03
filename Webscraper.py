import requests
from bs4 import BeautifulSoup

link = "https://worldcosplay.net/photo/6799292"
r = requests.get(link)
soup = BeautifulSoup(r.content, features="html.parser")
sause = soup.meta
print(sause)
