import pandas as pd

# dataset
data = [10, 30, 40, 60, 70, 80, 200]

s = pd.Series(data)
s1 = pd.Series(data, index= ["Row1", "Row2", "Row3", "Row4", "Row5", "Row6", "Row7"])
print("\n Print Data: \n", s1)


print("\n Print Index: \n", s1.index )


print("\n First 5 Element: \n", s.head())
print("\n First 2 Element: \n", s.head(2))
print("\n Last 5 Element: \n", s.tail())
print("\n Last 2 Element: \n", s.tail(2))


print("\n Series Information: \n", s.info())