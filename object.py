import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6, 4),columns=list('ABCD'))
print(df)
print(df.iloc[3])

# Adding new column E
df1 = df.reindex(columns=list(df.columns) + ['E'])
print(df1)

# drop rows that have missing data
print(df.dropna(how='any'))

# Filling Missing Values
print(df.fillna(value=5))
print("\n")

# Finding Mean
print("Finding Mean")
print(df.mean())
