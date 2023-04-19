import requests
from bs4 import BeautifulSoup
import shutil
import time
import os

link = "https://curecos.net/post/"
path = "/Users/peterfile/miniprograms/photos2"
place = open('place2.txt','r')

round = 1000             #number of download rounds per program run
set = 1000             #number of download atempts per round
num = int(place.read())
place.close()

sleep_time = 10

for i in range(0, round):

    for j in range(0, set):
        try:
            sauce = link + str(num + j)
            r = requests.get(sauce)
        except ConnectionResetError:
            print("cannot work " + sauce)
            print("\a")
            print("\a")
            r.close()
            time.sleep(120)
            continue

        if r.status_code == 200:

            soup = BeautifulSoup(r.content, features="html.parser")

            pics = soup.find(property="og:image")
            if pics == None or pics["content"] == "https://stg.curecos.netassets/icons/logo.png":
                print("cannot work " + sauce)
                continue

            pics_name = pics["content"].split('/')[-1]
            res = requests.get(pics["content"], stream = True)

            with open(os.path.join(path, pics_name), 'wb') as f:
                print(" Downloading: " + sauce + ' ' + pics_name)
                shutil.copyfileobj(res.raw, f)

            res.close()
        r.close()


    num += set

    print("Finished round: " + str(i+1))

    time.sleep(sleep_time)
place = open('place2.txt', 'w')
place.write(str(num))
place.close()
print("time to pop champain!")
print("\a")
