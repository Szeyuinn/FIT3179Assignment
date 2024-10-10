import pandas as pd

# Load the datasets (replace with your local paths or GitHub raw URLs if needed)
top10_path = "/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/data/runup_top10.csv"
allCountries_path = "/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/data/cleaned_data.csv"

# Load the CSVs
top10_df = pd.read_csv(top10_path)
allCountries_df = pd.read_csv(allCountries_path)

# Add the isTop10 flag
top10_df['isTop10'] = True
allCountries_df['isTop10'] = False

# Concatenate the two dataframes
merged_df = pd.concat([top10_df, allCountries_df])

# Save the merged dataframe to a new CSV
merged_csv_path = "/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/data/merged_runup_data.csv"
merged_df.to_csv(merged_csv_path, index=False)

print("Merged dataset saved to", merged_csv_path)
