import pandas as pd

file_path = '/Users/szeyuin/Documents/FIT3179/FIT3179Assignment/data/Historical_Tsunami_Event_Locations_with_Runups.csv'

# Load dataset from file path
df = pd.read_csv(file_path)

# Select only the necessary columns
columns_to_keep = ['YEAR', 'COUNTRY', 'RUNUP_HT', 'DEATHS', 'CAUSE']
cleaned_df = df[columns_to_keep]

cleaned_df_path = '/Users/szeyuin/Documents/FIT3179/FIT3179Assignment/data/cleaned_data.csv'
# Save the cleaned dataset to a new CSV file
cleaned_df.to_csv(cleaned_df_path, index=False)

print("Dataset cleaned and saved to '/Users/szeyuin/Documents/FIT3179/FIT3179Assignment/data/cleaned_data.csv'")
