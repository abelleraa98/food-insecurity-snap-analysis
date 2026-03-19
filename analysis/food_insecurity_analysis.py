import os
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load dataset
# -----------------------------
data = pd.read_csv("cleaned/state_food_insecurity_master.csv")

# Preview data
print(data.head())
print(data.columns)

# Make sure visualizations folder exists
os.makedirs("visualizations", exist_ok = True)

# -----------------------------
# 1. Top 10 States by Food Insecurity
# -----------------------------
plt.figure()

top10 = data.sort_values (by = "Food Insecurity Rate", ascending = False).head(10)

plt.bar(top10["State"], top10["Food Insecurity Rate"])

plt.title("Top 10 States by Food Insecurity")
plt.xlabel("State")
plt.ylabel("Food Insecurity Rate")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("visualizations/top10_food_insecurity.png")
plt.show()

# -----------------------------
# 2. Poverty vs Food Insecurity
# -----------------------------
plt.figure()

plt.scatter(data["Poverty Rate"], data["Food Insecurity Rate"])

plt.title("Poverty vs Food Insecurity")
plt.xlabel("Poverty Rate")
plt.ylabel("Food Insecurity Rate")

plt.tight_layout()

plt.savefig("visualizations/poverty_vs_food_insecurity.png")
plt.show()

# -----------------------------
# 3. Distribution
# -----------------------------
plt.figure()

plt.hist(
    data["Food Insecurity Rate"],
    bins=8,
    edgecolor="black"
)

mean_value = data["Food Insecurity Rate"].mean()
plt.axvline(mean_value, linestyle = "dashed")

plt.title("Distribution of Food Insecurity Rates Across States")
plt.xlabel("Food Insecurity Rate (%)")
plt.ylabel("Number of States")

plt.tight_layout()

plt.savefig("visualizations/food_insecurity_distribution.png")

plt.show()

# -----------------------------
# 4. SNAP Benefits vs Food Insecurity
# -----------------------------
plt.figure()

plt.scatter(data["SNAP Benefits"], data["Food Insecurity Rate"])

plt.title("SNAP Benefits vs Food Insecurity")
plt.xlabel("SNAP Benefits")
plt.ylabel("Food Insecurity Rate")

plt.tight_layout()

plt.savefig("visualizations/snap_benefits_vs_food_insecurity.png")

plt.show()