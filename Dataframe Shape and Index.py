#create pandas dataframe2

import pandas as pd

#dataset
data = {
    'Student' : ["Amit", "john", "klinton", "Fuad", "Akash"],
    'Rank': [1, 4, 3, 5, 2],
    'Marks': [95, 80, 75, 80, 90]
}

# Create a DataFrame using DataFrame() Method with index
df = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5'])     #it will show RowA.....RowE Bofore every row

print("Student Records \n", df)


# check Dataframe shape
print("\n Dimension: \n ", df.shape)
# check DataFrame index
print("\n Index: \n ", df.index)