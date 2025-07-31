#create pandas dataframe2

import pandas as pd

#dataset
data1 = {
    'Id': ["S1", "S2", "S3", "S4", "S5", "S6", "S7"],
    'Student': ["Amit", "john", "klinton", "Fuad", "Akash", "Ras", "sakib"],
    'Roll': [101, 102, 103, 104, 105, 106, 107]
}

data2 = {
    'Id': ["S8", "S9"],
    'Student': ["Chawhla", "Shimul"],
    'Roll': [108, 109]
}

# Create a DataFrame using DataFrame() Method with index
df1 = pd.DataFrame(data1, index = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7'])
df2 = pd.DataFrame(data2, index = ['Student8', 'Student9'])


print("\n DataFrame One Record:  \n", df1)
print("\n DataFrame Two Record:  \n", df2)


# Concat Two DataFrame
ConcatDataFrame  = pd.concat([df1, df2])

print("\n After Concatanation of two dataframe: \n", ConcatDataFrame)