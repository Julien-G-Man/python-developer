"""
Pandas makes it easier tp work with tabular data using DataFrames
"""

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Julien', 'Prince', 'Mike'],
    'Age': [25, 30, 20, 17, 28],
    'Program': ['Business Administration', 'Mechanical Engineering', 'Computer Science', 'Cyber Security', 'Law']
}
df = pd.DataFrame(data)
print(df)

# Load a CSV file and show the top 5 rows
print("\nFrom CSV File: wine_data.csv")
file1 = 'Files/wine_data.csv'
df1 = pd.read_csv(file1)
print(df1.head())

print('\nFrom CSV File: finance_data.csv')
file2 = 'Files/finance_data.csv'
df2 = pd.read_csv(file2)
print(df2)