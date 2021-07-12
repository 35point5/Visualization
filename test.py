import requests
from requests.api import request
#r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
r=requests.get('https://restapi.amap.com/v3/geocode/regeo',params={'key':'a1f20e56788bc5e9930326306872d63e','location':'111.43,21.97'})
j=r.json()
print(j)
print(j['regeocode']['addressComponent']['province'])