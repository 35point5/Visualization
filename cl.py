import numpy as np 
import pandas as pd
import calendar as cl

a=[[0,0,0,0,0,0,0],[50,50,40,50,2,100,35],[100,150,80,150,4,160,75],
   [150,475,180,250,14,215,115],[200,800,280,350,24,265,150],
   [300,1600,565,420,36,800,250],[400,2100,750,500,48,100,350],
   [500,2620,940,600,60,1200,500]]

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