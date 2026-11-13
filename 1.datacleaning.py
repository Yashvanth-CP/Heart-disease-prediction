import numpy as np
import pandas as pd 

df = pd.read_csv("heart-selected-columns.csv")
print(f"data : {df.describe()}")
print(df.head())
print(df.tail())

# Number of rows and columns
print(df.shape)

# Column names
print(df.columns)

# Dataset information
print(df.info())

# Statistical summary
print(df.describe())

# Check data types
print(df.dtypes)

# Check unique values
print(df.nunique())