import pandas as pd

# Access the spreadsheet and set row 8 as column headers
file_path = "/Users/femisokoya/Documents/GitHub/Buses/bus01.xlsx"
worksheet_name = "BUS01e"
df = pd.read_excel(file_path, sheet_name=worksheet_name, header=8)

# Delete rows 1-7 and column 15
df = df.iloc[6:].drop(columns=df.columns[15])

# Define the numeric columns where "[z]" can occur
numeric_columns = ['2009/10', '2010/11', '2011/12', '2012/13', '2013/14', '2014/15 ', '2016/17', '2017/18', '2018/19', '2019/20', '2020/21', '2021/22']  # Replace with actual column names

# Create a single notes column to store notes for all numeric columns
df['Notes'] = ""

# Loop through the numeric columns and insert "not applicable" for rows with '[z]' value
for column in numeric_columns:
    # Replace "[z]" occurrences with "not applicable" in the Notes column
    df.loc[df[column] == '[z]', 'Notes'] = 'not applicable'
    
    # Replace "[z]" occurrences with NaN in the original numeric columns
    df[column] = df[column].replace('[z]', pd.NA)

# Melt the dataframe to a long shape
df = df.melt(id_vars=['LA Code', 'Local Authority/ Region', 'Notes'],
             value_vars=numeric_columns, var_name="Period", value_name="Numerical")

# Convert any value '[z]' to 'E92000001' in column 0
df['LA Code'].replace('[z]', 'E92000001', inplace=True)

# Save the result in a CSV file
output_file = "test_with_notes.csv"
df.to_csv(output_file, index=False)

print("CSV file saved successfully.")
