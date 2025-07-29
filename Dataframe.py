#create pandas dataframe

import pandas as pd

#dataset
data = {
    'student' : ["Amit", "john", "klinton", "Fuad"],
    'rank': [1, 2, 3, 4],
    'marks': [95, 80, 75, 80]
}


df = pd.DataFrame(data)

print("Student Records \n", df)