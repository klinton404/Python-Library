#create pandas dataframe2

import pandas as pd

#dataset
data = {
    'Student' : ["Amit", "john", "klinton", "Fuad", "Akash"],
    'Rank': [1, 2, 3, 4, 5],
    'Marks': [95, 80, 75, 80, 90]
}


df = pd.DataFrame(data, index = ['RowA', 'RowB', 'RowC', 'RowD', 'RowE'])     #it will show RowA.....RowE Bofore every row

print("Student Records \n", df)


#Access the value of individual student
print("Student = ", df.loc['RowA', 'Student'])