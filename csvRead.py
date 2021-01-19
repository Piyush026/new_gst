import pandas

file = "cpm_data.csv"
df = pandas.read_csv(file, usecols=['CIN_Number', 'CompanyName'])
sd = df.values
tuples = [tuple(x) for x in df.values]
# print(tuples)
# for x in sd:
#     print(x)
# hi = list(df.index)
# print(hi)
# print(len(hi))
# print(type(hi))
