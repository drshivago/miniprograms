import requests
import random
from bs4 import BeautifulSoup
#import webbrowser
import shutil
import time
import os

link = "https://worldcosplay.net/photo/"
path = "/Users/peterfile/miniprograms/photos"
num = 14000
#max = 7040000
sleep_time = 240

random.seed

for i in range(0, 50):

    for x in range(0, 100):
        try:
            sauce = link + str(num + x)
            r = requests.get(sauce)
        except ConnectionError:
            print("cannot work " + sauce)
            r.close()
            time.sleep(120)
            continue

        if r.status_code == 200:

            soup = BeautifulSoup(r.content, features="html.parser")

            pics = soup.find(property="og:image")
            if pics == None:
                continue
            picsurl = pics["content"].split('/')[-1]
            res = requests.get(pics["content"], stream = True)

            with open(os.path.join(path, picsurl), 'wb') as f:
                shutil.copyfileobj(res.raw, f)
                print(" Downloading: " + sauce + ' ' + picsurl)

                #webbrowser.open_new_tab(pics)
    num += 100
    print("Waiting")
    r.close()
    res.close()
    time.sleep(sleep_time)
print("time to pop champain bitch")
