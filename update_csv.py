import csv

import pandas

"""update csv from another csv"""

gst_file = r'C:\Users\Administrator\Downloads\Smash\gst.csv'
df = pandas.read_csv(gst_file, usecols=['CompanyName', 'gst'])
csv_file = r'C:\Users\Administrator\Downloads\Smash\9.csv'
df1 = pandas.read_csv(csv_file, usecols=['CIN_Number', 'CompanyName'])
sd = df.merge(df1, how='inner', on='CompanyName')
print(sd)
hj = sd.dropna()
cols = list(hj.columns)
a, b = cols.index('gst'), cols.index('CIN_Number')
cols[b], cols[a] = cols[a], cols[b]
hj = hj[cols]
hj.to_csv("ghh.csv")
