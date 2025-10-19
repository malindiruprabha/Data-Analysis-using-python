import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("car.csv")
df.columns = df.columns.str.strip()  # Remove extra spaces if any
print(df.head())

# Use the exact column name from your CSV
sns.boxplot(x=df['Engine HP'])

plt.savefig("HP.png")
print("✅ Boxplot saved as 'HP.png'")
