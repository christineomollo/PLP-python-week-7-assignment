import pandas as pd
import seaborn as sns
# Reload iris.csv without using the first row as headers
df = pd.read_csv("iris.csv", header=None)

# assign proper names
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]


print(df.head())          # Check the first rows
print(df.columns)         # Confirm the new column names

 # Handle missing data
if df.isnull().values.any():
        print("Warning: Missing values detected. Filling with column means...")
        df.fillna(df.mean(numeric_only=True), inplace=True)

    # Ensure numeric columns have correct types
numeric_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")  # Convert invalid to NaN
if df[numeric_cols].isnull().values.any():
        print("Warning: Invalid numeric values found. Filling with means...")
        df.fillna(df.mean(numeric_only=True), inplace=True)
 

# Basic statistics of numerical columns
print(df.describe())
#Group by species and compute mean values of numerical columns
grouped_means = df.groupby("species").mean(numeric_only=True)
print(grouped_means)
import matplotlib.pyplot as plt

# 1. Line Chart (simulate "trends over samples")
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal_length"], label="Sepal Length", color="blue")
plt.plot(df.index, df["petal_length"], label="Petal Length", color="green")
plt.title("Line Chart: Sepal vs Petal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart (Average Petal Length per Species)
avg_petal = df.groupby("species")["petal_length"].mean()
plt.figure(figsize=(6,4))
avg_petal.plot(kind="bar", color=["skyblue","orange","lightgreen"])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram (Distribution of Sepal Length)
plt.figure(figsize=(6,4))
plt.hist(df["sepal_length"], bins=20, color="purple", edgecolor="black")
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()
# 4. Scatter Plot (Sepal Length vs Petal Length)
plt.figure(figsize=(6,5))
species_unique = df["species"].unique()
colors = ["red", "green", "blue"]

for sp, col in zip(species_unique, colors):
    subset = df[df["species"] == sp]
    plt.scatter(subset["sepal_length"], subset["petal_length"], label=sp, color=col)

plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

#  5. Line Chart (Sepal vs Petal Length across samples)
plt.figure(figsize=(8,5))
sns.lineplot(x=df.index, y="sepal_length", data=df, label="Sepal Length", color="pink")
sns.lineplot(x=df.index, y="petal_length", data=df, label="Petal Length", color="purple")
plt.title("Line Chart: Sepal vs Petal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()