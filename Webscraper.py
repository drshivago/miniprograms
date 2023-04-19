import requests
from bs4 import BeautifulSoup
import shutil
import time
import os

link = "https://worldcosplay.net/photo/"
path = "/Users/peterfile/miniprograms/photos"
with open('place.txt','r') as place:
    num = int(place.read())

round = 100            #number of download rounds per program run
set = 100               #number of download atempts per round

timer = time.time()
sleep_time = 10

for i in range(0, round):

    for j in range(0, set):
        try:
            sauce = link + str(num + j)
            r = requests.get(sauce)
        except Exception as e:
            print("cannot work " + sauce)
            print(f"Exception occured: {e}")
            print("\a")
            r.close()
            exit()

        if r.status_code == 200:

            soup = BeautifulSoup(r.content, features="html.parser")

            pics = soup.find(property="og:image")
            if pics == None:
                continue
            pics_name = pics["content"].split('/')[-1]
            res = requests.get(pics["content"], stream = True)

            with open(os.path.join(path, pics_name), 'wb') as f:
                shutil.copyfileobj(res.raw, f)
                print(" Downloading: " + sauce + ' ' + pics_name)
            res.close()
        r.close()

    num += set
    with open('place.txt', 'w') as place:
        place.write(str(num))

    print("Finished round: " + str(i+1))
    time.sleep(sleep_time)

print("time to pop champain!")
print("Time elapsed: " + "%.2f" % ((time.time() - timer)/60) + " Minutes")
print("\a")
