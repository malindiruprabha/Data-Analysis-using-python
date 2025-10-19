import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("car.csv")

# Clean column names (remove extra spaces)
df.columns = df.columns.str.strip()

# ✅ Select only numeric columns
numeric_df = df.select_dtypes(include='number')

# ✅ Compute correlation on numeric columns only
c = numeric_df.corr()

# ✅ Plot heatmap
plt.figure(figsize=(20, 10))
sns.heatmap(c, annot=True, cmap="BrBG", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_matrix.png")

print("✅ Correlation matrix saved as 'correlation_matrix.png'")
print(c)
