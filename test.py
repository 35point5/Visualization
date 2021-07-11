import numpy as np 
import pandas as pd
a=pd.read_csv("CN-Reanalysis-daily-2013010100.csv")
a.columns=['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'U(m/s)', 'V(m/s)', 'TEMP(K)', 'RH(%)', 'PSFC(Pa)', 'lat', 'lon','date']
#print(a[:5])
a['date']="2013-01-01"
a.to_csv('res.csv')
'''a=pd.read_csv('1.csv')
b=pd.read_csv('2.csv')
a=a.append(b)
print(a)
a.to_csv('res.csv')'''