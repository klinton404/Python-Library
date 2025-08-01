import pandas as pd

# dataset
data = [10, 30, 40, 60, 70, 80, 200]

s = pd.Series(data)     #index= ["Row1", "Row2", "Row3", "Row4", "Row5", "Row6", "Row7"]
print("\n Series: \n", s)



# Access a Value
print("\n Value From Pandas Series: \n", s[2])


s1 = pd.Series(data, index= ["Row1", "Row2", "Row3", "Row4", "Row5", "Row6", "Row7"])
print("\n Print Row D: \n", s1["Row4"])