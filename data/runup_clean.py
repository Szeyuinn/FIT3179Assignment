import pandas as pd

# Load the dataset
df = pd.read_csv("/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/data/cleaned_data.csv")

# Drop rows where 'RUNUP_HT' is null
df_clean = df.dropna(subset=["RUNUP_HT"])

# Group by 'COUNTRY' and calculate the sum or mean of 'RUNUP_HT'
df_grouped = df_clean.groupby("COUNTRY").agg(
    total_runup_ht=pd.NamedAgg(column="RUNUP_HT", aggfunc="sum")  # Use 'sum', 'median', or 'mean' depending on your criteria
).reset_index()

# Sort the countries by total run-up height in descending order
df_sorted = df_grouped.sort_values(by="total_runup_ht", ascending=False)

# Select the top 10 countries
df_top10 = df_sorted.head(10)

# Merge the filtered top 10 countries back with the original cleaned data to keep all other columns
df_filtered = df_clean[df_clean['COUNTRY'].isin(df_top10['COUNTRY'])]

# Save the filtered dataset to a new CSV file
df_filtered.to_csv("/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/data/runup_top10.csv", index=False)

print("Filtered dataset saved as filtered_top10_data.csv")
