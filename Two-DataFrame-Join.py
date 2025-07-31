#create pandas dataframe2

import pandas as pd

#dataset
data1 = {
    'id': ["S1", "S2", "S3", "S4", "S5", "S6", "S7"],
    'Student': ["Amit", "john", "klinton", "Fuad", "Akash", "Ras", "sakib"],
    'Roll': [101, 102, 103, 104, 105, 106, 107]
}

data2 = {
    'Rank': [1, 4, 3, 5, 2, 7, 6],
    'Marks': [95, 80, 75, 80, 90, 99, 92]
}

# Create a DataFrame using DataFrame() Method with index
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


print("\n DataFrame One Record:  \n", df1)
print("\n DataFrame Two Record:  \n", df2)


# Joining Two DataFrame
JoinDF = df1.join(df2)

print("\n After joining two dataframe: \n", JoinDF)