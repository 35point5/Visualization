import requests
import numpy as np 
import pandas as pd
import calendar as cl
from requests.api import request
'''r=requests.get('https://restapi.amap.com/v3/geocode/regeo',params={'key':'a1f20e56788bc5e9930326306872d63e','location':'111.43,21.97'})
j=r.json()
print(j)
print(j['regeocode']['addressComponent']['province'])'''
ind=pd.DataFrame({'lat':[],'lon':[],'province':[],'adcode':[]})
now=pd.read_csv('data.csv')
print(now)
for i in range(0,now.shape[0]):
    s=str(now.at[i,' lon'])+','+str(now.at[i,' lat'])
    r=requests.get('https://restapi.amap.com/v3/geocode/regeo',params={'key':'a1f20e56788bc5e9930326306872d63e','location':s})
    j=r.json()
    ind=ind.append([{'lat':now.at[i,' lat'],'lon':now.at[i,' lon'],'province':j['regeocode']['addressComponent']['province'],'adcode':j['regeocode']['addressComponent']['adcode']}],ignore_index=True)
    print(i)

ind.to_csv('map.csv')