import csv

import pandas

"""update csv from another csv"""

gst_file = '/home/ezeia/PycharmProjects/GST_Scraper/cmp_gst.csv'
df = pandas.read_csv(gst_file, usecols=['CompanyName', 'pan'])
csv_file = '/home/ezeia/Downloads/6.csv'
df1 = pandas.read_csv(csv_file, usecols=['CIN_Number', 'CompanyName'])
sd = df1.merge(df, how='inner', on='CompanyName')
print(sd)
hj = sd.dropna()
hj.to_csv("ghh.csv")
