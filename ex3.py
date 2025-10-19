import pandas as pd
import numpy as np       
import matplotlib.pyplot as plt   
import seaborn as sns
sns.set(color_codes=True)
df = pd.read_csv("car.csv")
print(df.head())
print(df.dtypes)
print(df.columns)
print(df.columns.values)
print('/n')
#Analytical Summary of the Dataset
print(df.describe(include='all'))
df.hist(figsize=(20, 30)) # Correct method
plt.show()

