import pandas as pd

from datetime import datetime, timedelta
date = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')


j= 0
s=''
while j<10:
    if (j==4) or (j==7):
        j+=1
    else:
        s = s+date[j]
        j+=1
#print (int(s))


data = pd.read_csv('CSVdataframe1.csv',names = [
                              'country symbol',
                              'country',
                              'rupee to foreign',
                              'foreign to rupee',
                              'year'],
                   encoding = 'latin-1',index_col = 0)


data = data.convert_objects(convert_numeric = True)
#data['YYYYMMDD'] = s

del data['rupee to foreign']
del data['country']
del data['year']


##data_correlation = data.corr()
##print (data_correlation)
##print (data_correlation.describe())

print (data['country symbol'])




