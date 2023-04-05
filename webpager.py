import requests
from bs4 import BeautifulSoup
import webbrowser

link = "https://worldcosplay.net/photo/"

for x in range(0, 50000):

    sauce = link + str(x)
    r = requests.get(sauce)
    if r.status_code == 200:

        #soup = BeautifulSoup(r.content, features="html.parser")
        #sauce = soup.find(property="og:image")["content"]
        #print(sauce)
        #res = requests.get(sauce, stream = True)


        webbrowser.open_new_tab(sauce)
