import pandas

file = "/home/ezeia/PycharmProjects/geekforgeeks/csv/ghh.csv"
df = pandas.read_csv(file, usecols=['CIN_Number', 'pan'])
sd = df.values
tuples = [tuple(x) for x in df.values]
print(tuples)
# print(tuples)
# for x in sd:
#     print(x)
# hi = list(df.index)
# print(hi)
# print(len(hi))
# print(type(hi))
