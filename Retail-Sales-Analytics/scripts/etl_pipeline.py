import pandas as pd

# Load dataset
df = pd.read_csv("data/retail_sales.csv")

# --- Introduce some dummy issues for testing ---
# 1. Add duplicates
df = pd.concat([df, df.iloc[:2]], ignore_index=True)

# 2. Set one TotalAmount value to NaN
df.loc[1, "TotalAmount"] = None

# 3. Make one Product name missing
df.loc[3, "Product"] = None

print("Before Cleaning: ", df.shape)

# --- Clean missing values ---
df.dropna(subset=["Product"], inplace=True)

# Fill missing TotalAmount where possible
df["TotalAmount"].fillna(df["Quantity"] * df["UnitPrice"], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("After Cleaning: ", df.shape)

# Save cleaned dataset
df.to_csv("data/retail_sales_cleaned.csv", index=False)

print("Data cleaning completed. Clean file saved at: data/retail_sales_cleaned.csv")
