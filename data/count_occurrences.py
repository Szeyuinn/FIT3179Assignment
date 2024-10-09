import pandas as pd
import json

# Load TopoJSON
topojson_path = '/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/js/ne_110m.json'
with open(topojson_path, 'r') as f:
    topojson = json.load(f)

# Extract country names from the TopoJSON
countries_in_topojson = [feature['properties']['NAME_LONG'] for feature in topojson['objects']['ne_110m_admin_0_countries']['geometries']]

# Convert to lowercase for matching
countries_in_topojson = [country.lower() for country in countries_in_topojson]

# Load your dataset
file_path = '/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/data/cleaned_data.csv'
data = pd.read_csv(file_path)

# Filter the dataset to include only years greater than or equal to 1800
data = data[data['YEAR'] >= 1800]

# Create a mapping dictionary for country name replacements
country_mapping = {
    'Uk': 'United Kingdom',
    'Uk Territory': 'United Kingdom',
    'USA': 'United States',
    'USA Territory': 'United States',
    # Add other mappings if necessary
}

# Apply the mapping to the 'COUNTRY' column
data['COUNTRY'] = data['COUNTRY'].replace(country_mapping)

# Convert 'COUNTRY' names to lowercase for matching
data['COUNTRY'] = data['COUNTRY'].str.lower()

# Filter the dataset to keep only countries that exist in the TopoJSON
filtered_data = data[data['COUNTRY'].isin(countries_in_topojson)]

# Group by 'COUNTRY' and 'YEAR' and count occurrences for each year
country_year_occurrences = filtered_data.groupby(['COUNTRY', 'YEAR']).size().reset_index(name='OCCURRENCES')

# Fill any NaN values in OCCURRENCES with 0
country_year_occurrences['OCCURRENCES'] = country_year_occurrences['OCCURRENCES'].fillna(0)

# Convert country names to Title Case to match TopoJSON format
country_year_occurrences['COUNTRY'] = country_year_occurrences['COUNTRY'].str.title()

# Save the filtered occurrences to a new CSV for use in Vega-Lite
result_path = '/Users/szeyuin/Documents/FIT3179/FIT3179Assignment-1/data/country_year_occurrences.csv'
country_year_occurrences.to_csv(result_path, index=False)


