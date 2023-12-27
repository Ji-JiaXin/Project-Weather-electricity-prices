import pandas as pd

file_path = 'C:/Users/Sedláček/OneDrive - FSV/Documents/DataProcessingPython/Project-Weather-electricity-prices/C1KOCE01.xlsx'

# Read the Excel file
df = pd.read_excel(file_path, sheet_name='teplota průměrná')


print(df)