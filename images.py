import tkinter  # py3
from PIL import Image, ImageTk
import time
import requests
from bs4 import BeautifulSoup
import shutil
import os
#
root = tkinter.Tk()
#imname = "photos/8d41bf1504d942ae4c3b4236ebbc22b04aacfc0d-740.jpg"
# PIL Images
# adapters for tkinter
#im2 = ImageTk.PhotoImage(Image.open(imname))
# These can be used everywhere Tkinter expects an image object.
#tkinter.Label(root, image=im2, bd=0).grid(row=0, column=0)


link = "https://worldcosplay.net/photo/"
path = "/Users/peterfile/miniprograms/photos/"
num = 5

round = 1             #number of download rounds per program run
set = 5               #number of download atempts per round


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
            exit()

        if r.status_code == 200:                                 #if page exists

            soup = BeautifulSoup(r.content, features="html.parser")

            pics = soup.find(property="og:image")
            if pics == None:
                continue
            pics_name = pics["content"].split('/')[-1]
            res = requests.get(pics["content"], stream = True)

            with open(os.path.join(path, pics_name), 'wb') as f:
                shutil.copyfileobj(res.raw, f)
                print(" Downloading: " + sauce + ' ' + pics_name)
            im2 = ImageTk.PhotoImage(Image.open(os.path.join(path, pics_name)))
            tkinter.Label(root, image=im2, bd=0).grid(row=0, column=0)
            root.update()
            res.close()
        else:
            print("/",end="")
        r.close()

    num += set
    print()
    print("Finished round: ", i+1)
    time.sleep(sleep_time)
