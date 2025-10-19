
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")  # 🔄 Use non-GUI backend
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("car.csv")

#Relation between categorical and continuous variables
# Create the boxplot
sns.boxplot(x='Vehicle Size', y='Engine HP', data=df)

# Save plot to file instead of showing it
plt.savefig("boxplot.png")
print("✅ Boxplot saved as 'boxplot.png'")