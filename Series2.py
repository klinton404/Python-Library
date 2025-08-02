import numpy as np
import pandas as pd

# dataset
data = [10, 30, 40, 60, 70, 80, 200, np.nan]

s = pd.Series(data)
print(s)
print("\n Does the series has NaN: ?", s.hasnans)