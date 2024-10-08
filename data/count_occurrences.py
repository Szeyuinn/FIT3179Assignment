import pandas as pd

# Load the dataset
file_path = '/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/data/cleaned_data.csv'
data = pd.read_csv(file_path)

# Group by 'COUNTRY' and 'YEAR' and count occurrences for each year
country_year_occurrences = data.groupby(['COUNTRY', 'YEAR']).size().reset_index(name='OCCURRENCES')

result_path = '/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/data/country_year_occurrences.csv'
# Save the occurrences to a new CSV for use in Vega-Lite
country_year_occurrences.to_csv(result_path, index=False)

