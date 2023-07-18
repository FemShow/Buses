
import pandas as pd

# Access the spreadsheet
file_path = "/Users/femisokoya/Documents/GitHub/Buses/bus01.xlsx"
worksheet_name = "BUS01e"
df = pd.read_excel(file_path, sheet_name=worksheet_name)

# Delete rows 1-7
df = df.iloc[6:]

# Delete column 15
df = df.drop(columns=df.columns[15])

# Set row 8 as column headers
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header

# Melt the dataframe to a long shape
df = df.melt(id_vars=['LA Code', 'Local Authority/ Region'])

# Save the result in a CSV file
output_file = "test.csv"
df.to_csv(output_file, index=False)

print("CSV file saved successfully.")