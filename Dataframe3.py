#create pandas dataframe2

import pandas as pd

#dataset
data = {
    'Student' : ["Amit", "john", "klinton", "Fuad", "Akash"],
    'Rank': [1, 4, 3, 5, 2],
    'Marks': [95, 80, 75, 80, 90]
}


df = pd.DataFrame(data, index = ['RowA', 'RowB', 'RowC', 'RowD', 'RowE'])     #it will show RowA.....RowE Bofore every row

print("Student Records \n", df)


# Access using row and column by integer position   (  df.iloc[]   )
print("\n Student = \n", df.iloc[[1, 2]])