#create pandas dataframe2

import pandas as pd

#dataset
data = {
    'Student' : ["Amit", "john", "klinton", "Fuad", "Akash", "Ras", "sakib"],
    'Rank': [1, 4, 3, 5, 2, 7, 6],
    'Marks': [95, 80, 75, 80, 90, 99, 92]
}

# Create a DataFrame using DataFrame() Method with index
df = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7'])     #it will show RowA.....RowE Bofore every row

print("Student Records \n", df)



# It will print only 5 row
print("\n First 5 row: \n ", df.head())