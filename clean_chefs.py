import pandas as pd

df = pd.read_csv("chefs_raw.csv")

print("ORIGINAL DATA")
print(df)

# Standardize names
df["name"] = df["name"].str.title()

# Standardize emails
df["email"] = df["email"].str.lower()

# Remove duplicated rows
df = df.drop_duplicates()

print("\nCLEANED DATA")
print(df)

# Save cleaned file
df.to_csv(
    "chefs_clean.csv",
    index=False
)

print("\nCleaning completed")