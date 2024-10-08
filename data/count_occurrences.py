import pandas as pd

# Load the dataset
file_path = '/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/data/cleaned_data.csv'
data = pd.read_csv(file_path)

# Filter the dataset to include only years greater than or equal to 1800
data = data[data['YEAR'] >= 1800]

# Convert country names to Title Case to match TopoJSON format
data['COUNTRY'] = data['COUNTRY'].str.title()

# # Group by 'COUNTRY' and 'YEAR' and count occurrences for each year
# country_year_occurrences = data.groupby(['COUNTRY', 'YEAR']).size().reset_index(name='OCCURRENCES')

# Group by 'COUNTRY' only and sum up all occurrences
country_year_occurrences = data.groupby(['COUNTRY']).agg({'OCCURRENCES': 'sum'}).reset_index()

# Fill any NaN values in OCCURRENCES with 0
country_year_occurrences['OCCURRENCES'] = country_year_occurrences['OCCURRENCES'].fillna(0)

# Save the occurrences to a new CSV for use in Vega-Lite
result_path = '/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/data/country_year_occurrences.csv'
country_year_occurrences.to_csv(result_path, index=False)

