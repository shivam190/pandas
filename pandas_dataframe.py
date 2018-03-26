# creates data frame using random numbers for 2D array
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6, 4),columns=list('ABCD'))
print(df)
print("\n")
print(df.index)
print("\n")
print(df.columns)
print("\n")
print(df.values)
