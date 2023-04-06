import requests
import random
from bs4 import BeautifulSoup
import webbrowser
import shutil
import time
import os

link = "https://worldcosplay.net/photo/"
random.seed
random_max = 7040000
sleep_time = 60
path = "/Users/peterfile/miniprograms/photos"

for i in range(0, 10):
    for x in range(0, 100):

        sauce = link + str(random.randrange(0, random_max))
        r = requests.get(sauce)
        if r.status_code == 200:

            soup = BeautifulSoup(r.content, features="html.parser")
            pics = soup.find(property="og:image")["content"]
            print("Downloading: " + sauce)
            res = requests.get(pics, stream = True)

            with open(os.path.join(path, (pics.split('/')[-1])), 'wb') as f:
                shutil.copyfileobj(res.raw, f)
                #webbrowser.open_new_tab(pics)

print("Waiting")
r.close()
res.close()
time.sleep(sleep_time)
