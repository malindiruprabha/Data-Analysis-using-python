import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("car.csv")


# Use the actual column name you printed
sns.boxplot(x=df['MSRP'])  # Replace with your actual column name

plt.savefig("MSRP.png")
print("✅ Boxplot saved as 'MSRP.png'")
