import pandas as pd

# Load the first CSV file (2010 data)
df1 = pd.read_csv('postcode_information_10_nov_2010.csv', low_memory=False)

# Load the second CSV file (2015 data)
df2 = pd.read_csv('postcode_information_15_jul_2015.csv', low_memory=False)

# Identify the postcode columns in both datasets
postcode_column_1 = 'PCD10nov'  # Postcode column in the 2010 dataset
postcode_column_2 = 'PCD15jul'  # Postcode column in the 2015 dataset

# Clean postcodes by stripping whitespace and converting to uppercase
df1[postcode_column_1] = df1[postcode_column_1].str.strip().str.upper()
df2[postcode_column_2] = df2[postcode_column_2].str.strip().str.upper()

# Extract the unique postcodes from both datasets as sets (this makes the comparison faster)
postcodes_df1 = set(df1[postcode_column_1].dropna().unique())
postcodes_df2 = set(df2[postcode_column_2].dropna().unique())

# Identify unmatched postcodes from the 2010 dataset (using set difference for faster comparison)
unmatched_postcodes_2010 = postcodes_df1 - postcodes_df2

# Convert the unmatched postcodes into a DataFrame and save them to a CSV file
unmatched_df_2010 = pd.DataFrame(list(unmatched_postcodes_2010), columns=[postcode_column_1])
unmatched_df_2010.to_csv('unmatched_postcodes_from_10_nov_2010.csv', index=False)

print(f"Unmatched postcodes from 10 Nov 2010 have been saved to 'unmatched_postcodes_from_10_nov_2010.csv'")
