import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")  # ✅ Non-interactive backend
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("car.csv")

# Create pairplot
pairplot = sns.pairplot(df)

# Save the plot
pairplot.savefig("pairplot.png")
print("✅ Pairplot saved as 'pairplot.png'")
