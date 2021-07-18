import numpy as np 
import pandas as pd
import calendar as cll

temp={'date':[],'IAQI':[],'IAQI_SO2':[],'IAQI_NO2':[],'IAQI_PM10':[],'IAQI_CO':[],'IAQI_O3':[],'IAQI_PM25':[],'Temp':[],'Press':[]}
ind={}
now=pd.read_csv("./prov/2013_1_1.csv")
for i in range(0,now.shape[0]):
    ind[now.at[i,'province']]=pd.DataFrame(temp)
for year in [2013,2014,2015,2016]:
    for month in range(1,13):
        for day in range(1,cll.monthrange(year,month)[1]+1):
            now=pd.read_csv('./prov/'+str(year)+'_'+str(month)+'_'+str(day)+'.csv')
            for i in range(0,now.shape[0]):
                ind[now.at[i,'province']]=ind[now.at[i,'province']].append({'date':str(year)+'-'+str(month).zfill(2)+'-'+str(day).zfill(2),'IAQI':now.at[i,'IAQI'],'IAQI_SO2':now.at[i,'IAQI_SO2'],'IAQI_NO2':now.at[i,'IAQI_NO2'],'IAQI_PM10':now.at[i,'IAQI_PM10'],'IAQI_CO':now.at[i,'IAQI_CO'],'IAQI_O3':now.at[i,'IAQI_O3'],'IAQI_PM25':now.at[i,'IAQI_PM25'],'Temp':now.at[i,'TEMP(K)'],'Press':now.at[i,'PSFC(Pa)']},ignore_index=True)
            print(str(year)+'-'+str(month).zfill(2)+'-'+str(day).zfill(2))
for i in ind:
    #ind[i].T.to_json('./date/'+i+'.json')
    ind[i].to_csv('./date/'+i+'.csv')
    
