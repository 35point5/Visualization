import numpy as np 
import pandas as pd
import calendar as cl

a=[[0,0,0,0,0,0,0],[50,50,40,50,2,100,35],[100,150,80,150,4,160,75],
   [150,475,180,250,14,215,115],[200,800,280,350,24,265,150],
   [300,1600,565,420,36,800,250],[400,2100,750,500,48,100,350],
   [500,2620,940,600,60,1200,500]]

def cl(id,val):
    for i in range(7):
        if val>=a[i][id] and val<=a[i+1][id]:
            return 1.0*(a[i+1][0]-a[i][0])/(a[i+1][id]-a[i][id])*(val-a[i][id])+a[i][0]
    return 500.0

temp={'PM2.5':[], 'PM10':[], 'SO2':[], 'NO2':[], 'CO':[], 'O3':[], 'U(m/s)':[], 'V(m/s)':[], 'TEMP(K)':[], 'RH(%)':[], 'PSFC(Pa)':[], 'lat':[], 'lon':[],'date':[]}
ind=pd.DataFrame(temp)
path='./data/2014'
#print(path+"{:0>2d}".format(5))
l={0:2,1:3,2:1,3:4,4:5,5:0}
for i in range(1,2):
    for j in range(1,2):#cl.monthrange(2014,i)[1]):
#        print(path+"{:0>2d}".format(i)+'/'+'CN-Reanalysis-daily-2014'+"{:0>2d}".format(i)+"{:0>2d}".format(j)+'00.csv')
        now=pd.read_csv(path+"{:0>2d}".format(i)+'/'+'CN-Reanalysis-daily-2014'+"{:0>2d}".format(i)+"{:0>2d}".format(j)+'00.csv')
        now.columns=['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'U(m/s)', 'V(m/s)', 'TEMP(K)', 'RH(%)', 'PSFC(Pa)', 'lat', 'lon','date']
        now['date']='2014-'+str(i)+'-'+str(j)
        now['IAQI_SO2']=0
        now['IAQI_NO2']=0
        now['IAQI_PM10']=0
        now['IAQI_CO']=0
        now['IAQI_O3']=0
        now['IAQI_PM25']=0

        for k in range(0,now.shape[0]):
            for t in range(6):
                now.iat[k,14+t]=cl(t+1,now.iat[k,l[t]])

        print(now)
        print(now.iat[1,3])

        
