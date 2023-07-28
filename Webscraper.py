import requests
from bs4 import BeautifulSoup
import shutil
import time
import os

def timeDivider(time, amount):
    unit = time % amount
    temp_time = time - unit
    temp_time = temp_time // amount
    return temp_time, unit

def timeDecorator(time_date):

    if time_date < 60:
        return 0, 0, 0, time_date
    time_date, seconds = timeDivider(time_date, 60)
    time_date, minutes = timeDivider(time_date, 60)
    days, hours = timeDivider(time_date, 24)

    return days, hours, minutes, seconds

link = "https://worldcosplay.net/photo/"
home = "/Users/peterfile/miniprograms/photos/"

with open('place.txt','r') as place:
    num = int(place.readline())
    file_num = int(place.readline())
    photo_saves = int(place.readline())

round = 10000               #number of download rounds per program run
set = 100                   #number of download atempts per round
retry = 0                   #don't fail twice
sleep_time = 10
timer = time.time()
session = requests.Session()
path = os.path.join(home, str(file_num))

for i in range(0, round):

    for j in range(0, set):
        try:
            sauce = link + str(num + j)
            r = session.get(sauce, timeout = 60)

            if r.status_code == 200:                                                    #if page exists

                soup = BeautifulSoup(r.text, features="html.parser")
                pics = soup.find(property="og:image")

                if pics == None:
                    continue
                res = session.get(pics["content"], stream = True, timeout = 60)
                pics_name = pics["content"].split('/')[-1]

                with open(os.path.join(path, pics_name), 'wb') as f:                    #Save file
                    shutil.copyfileobj(res.raw, f)
                    photo_saves += 1
                    print(" Downloading: " + sauce + ' ' + pics_name)

            else:
                print("/",end="")

        except Exception as e:
            print("\ncannot work " + sauce)
            print(f"Exception occured: {e}")

            if retry == num + j:
                with open('place.txt', 'w') as place:                           #failed 2 in row, save progress and quit
                    place.write(str(num) + '\n')
                    place.write(str(file_num) + '\n')
                    place.write(str(photo_saves))
                print("\a", "\a", "\a")
                exit()
            else:
                print("\a", "\a")                                               #stop and retry in 5 min
                retry = num + j
                num -= 1
                time.sleep(600)
                continue

    num += set
    if photo_saves >= 50000:                                                    #if files ~50000 make new folder, use that

        file_num += 1
        path = os.path.join(home, str(file_num))
        os.mkdir(path)
        print("Making new folder")
        photo_saves = 0

    with open('place.txt', 'w') as place:                                       #save progress
        place.write(str(num) + '\n')
        place.write(str(file_num) + '\n')
        place.write(str(photo_saves))
    print()
    print("Finished round: ", i+1)
    session.close()
    time.sleep(sleep_time)

print("time to pop champain!")                                                  #some how finised without error
time_elaps = timeDecorator(int(time.time() - timer))
print("Time elapsed: ", time_elaps[0], " days ", time_elaps[1], " hours ",\
time_elaps[2], " minutes ", time_elaps[3], " seconds")
print("\a")
