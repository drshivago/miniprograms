import requests
import random
from bs4 import BeautifulSoup
#import webbrowser
import shutil
import time
import os

link = "https://worldcosplay.net/photo/"
path = "/Users/peterfile/miniprograms/photos"
random_min = 14000
random_max = 7040000
sleep_time = 300

random.seed

for i in range(0, 10):

    for x in range(0, 100):
        try:
            sauce = link + str(random.randrange(random_min, random_max))
            r = requests.get(sauce)
        except ConnectionError:
            print("cannot work " + sauce)
            r.close()
            time.sleep(120)
            continue

        if r.status_code == 200:

            soup = BeautifulSoup(r.content, features="html.parser")
            print(str(x) + " Downloading: " + sauce)
            pics = soup.find(property="og:image")
            if pics == None:
                continue

            res = requests.get(pics["content"], stream = True)

            with open(os.path.join(path, (pics["content"].split('/')[-1])), 'wb') as f:
                shutil.copyfileobj(res.raw, f)
                #webbrowser.open_new_tab(pics)

    print("Waiting")
    r.close()
    res.close()
    time.sleep(sleep_time)
print("time to pop champain bitch")
