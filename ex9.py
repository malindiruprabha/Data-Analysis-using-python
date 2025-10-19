import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("car.csv")
print(df.head())
df.columns = df.columns.str.strip()  # Remove extra spaces if any
#platting a Histogram  for  number of cars per barand
df['Make'].value_counts().nlargest(40).plot(kind='bar', figsize=(12, 6))

plt.title('Number of Cars per Brand')
plt.xlabel('Car Brand')
plt.ylabel('Number of Cars')
plt.savefig("cars_per_brand.png")
print("✅ Histogram saved as 'cars_per_brand.png'")