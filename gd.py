import numpy as np 
import pandas as pd
import calendar as cl
temp={'PM2.5':[], 'PM10':[], 'SO2':[], 'NO2':[], 'CO':[], 'O3':[], 'U(m/s)':[], 'V(m/s)':[], 'TEMP(K)':[], 'RH(%)':[], 'PSFC(Pa)':[], 'lon':[],'date':[]}
ind=pd.DataFrame(temp)
path='./data/2014'
#print(path+"{:0>2d}".format(5))
for i in range(1,3):
    for j in range(1,cl.monthrange(2014,i)[1]+1):
        print(j)
#        print(path+"{:0>2d}".format(i)+'/'+'CN-Reanalysis-daily-2014'+"{:0>2d}".format(i)+"{:0>2d}".format(j)+'00.csv')
        now=pd.read_csv(path+"{:0>2d}".format(i)+'/'+'CN-Reanalysis-daily-2014'+"{:0>2d}".format(i)+"{:0>2d}".format(j)+'00.csv')
        #print(now.shape[0]//100)
        p=50
        for k in range(0,now.shape[0]//p):
            now.iat[k*p,11]=str(now.iat[k*p,12])+','+str(now.iat[k*p,11])
#        for k in range(0,now.shape[0]):
#            now.iat[k,11]=str(now.iat[k,12])+','+str(now.iat[k,11])
        now=now.drop([" lon"],axis=1)
        #print(now)
        now.columns=['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'U(m/s)', 'V(m/s)', 'TEMP(K)', 'RH(%)', 'PSFC(Pa)', 'lon','date']
        now['date']='2014-'+str(i)+'-'+str(j)
        for k in range(0,now.shape[0]//p):
            ind=ind.append(now[k*p:k*p+1])
#        ind=ind.append(now)
        
print(ind)
ind.to_csv('gd1.csv')