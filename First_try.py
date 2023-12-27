import pandas as pd

# Read the TSV file
file_path = 'C:/Users/Sedláček/OneDrive - FSV/Documents/DataProcessingPython/Project-Weather-electricity-prices/Consumption.csv'
df = pd.read_csv(file_path, sep=';')

# Select the columns you want for the new DataFrame
columns_to_include = ['Date', 'Total (grid load) [MWh] Calculated resolutions',
                       'Residual load [MWh] Calculated resolutions',
                         'Hydro pumped storage [MWh] Calculated resolutions']

# Create the new DataFrame with only the selected columns
new_df = df[columns_to_include]

df = new_df

rename_dict = {
    'Total (grid load) [MWh] Calculated resolutions': 'Tot_cons',
    'Residual load [MWh] Calculated resolutions': 'Res_load',
    'Hydro pumped storage [MWh] Calculated resolutions' : 'Hydro_pumped'
}

# Rename the columns
df.rename(columns=rename_dict, inplace=True)

# Check the new column names
print(df.columns)

df.to_csv('new_file.csv', sep=';', index=True)
