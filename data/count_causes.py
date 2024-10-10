import pandas as pd

# Load your dataset
df = pd.read_csv('/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/data/cleaned_data.csv')

# Remove rows where 'CAUSE' is empty or NaN
df_cleaned = df[df['CAUSE'].notna() & (df['CAUSE'] != ' ')]

# Count occurrences of each cause
cause_counts = df_cleaned['CAUSE'].value_counts().reset_index()

# Rename the columns to match the expected format
cause_counts.columns = ['text', 'size']

# Display the cleaned dataset
print(cause_counts)

# Save the cleaned data as a JSON file
cause_counts.to_json('cleaned_causes.json', orient='records')
