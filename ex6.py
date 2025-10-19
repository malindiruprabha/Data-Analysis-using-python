import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")  # ✅ Non-interactive backend
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("car.csv")
df = df.drop(['Engine Fuel Type', 'Market Category','Vehicle Style','Popularity','Number of Doors','Vehicle Size'], axis=1)
print(df.head(5))
df = df.rename(columns={'Engine HP': 'HP', 'Engine Cylinders': 'Cylinders', 'Transmission Type': 'Type'})
print(df.head(5))
print(df.shape) # Total number of rows and columns
# Rows containing duplicate data
duplicate_rows_df = df[df.duplicated()]
print("Number of duplicate rows: ", duplicate_rows_df.shape )
#Count the rows before removing data
print(df.count())
#Drop the duplicates
df = df.drop_duplicates()
print(df.head())
print(df.count())
print('/n')
#Find the null values
print(df.isnull().sum())
#Drop the missing Values
df = df.dropna()
print(df.count())
print('/n')
print(df.isnull().sum())
