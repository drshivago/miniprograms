import requests
from bs4 import BeautifulSoup
import shutil

link = "https://worldcosplay.net/photo/6799292"
#name = "image"
#add json reading bit here
r = requests.get(link)
soup = BeautifulSoup(r.content, features="html.parser")
sauce = soup.find(property="og:image")["content"]
print(sauce)
res = requests.get(sauce, stream = True)

if res.status_code == 200:
    with open(sauce[36:-4] + '.jpg', 'wb') as f:
        shutil.copyfileobj(res.raw, f)
