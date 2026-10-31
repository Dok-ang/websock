import requests
from bs4 import BeautifulSoup # клас який дозволяє розібрати html
url="https://worldoftanks.com/"
r=requests.get(url)
print(r.text)
#soup=BeautifulSoup(r.text,"html.parser")
#print(soup.find("h1"))