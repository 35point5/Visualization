import numpy as np 
import pandas as pd
import calendar as cl
temp={'PM2.5':[], 'PM10':[], 'SO2':[], 'NO2':[], 'CO':[], 'O3':[], 'U(m/s)':[], 'V(m/s)':[], 'TEMP(K)':[], 'RH(%)':[], 'PSFC(Pa)':[], 'lat':[], 'lon':[],'date':[]}
ind=pd.DataFrame(temp)
path='./data/2014'
#print(path+"{:0>2d}".format(5))
for i in range(1,2):
    for j in range(1,cl.monthrange(2014,i)[1]):
#        print(path+"{:0>2d}".format(i)+'/'+'CN-Reanalysis-daily-2014'+"{:0>2d}".format(i)+"{:0>2d}".format(j)+'00.csv')
        now=pd.read_csv(path+"{:0>2d}".format(i)+'/'+'CN-Reanalysis-daily-2014'+"{:0>2d}".format(i)+"{:0>2d}".format(j)+'00.csv')
        now.columns=['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'U(m/s)', 'V(m/s)', 'TEMP(K)', 'RH(%)', 'PSFC(Pa)', 'lat', 'lon','date']
        now['date']='2014-'+str(i)+'-'+str(j)
        for k in range(0,now.shape[0]//100):
            ind=ind.append(now[k*100:k*100+1])
        
print(ind)
ind.to_csv('res.csv')