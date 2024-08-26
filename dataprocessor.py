# import csv

# with open('train_data.csv', 'r') as input_file:
#     reader = csv.reader(input_file)
#     with open('output.csv', 'w', newline='') as output_file:
#         writer = csv.writer(output_file)
#         for row in reader:
#             if any(field.strip() for field in row):
#                 writer.writerow(row)

import pandas as pd

# Define the path to your CSV file
csv_file_path = 'test_data.csv'  # Replace with your CSV file path

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Remove rows with any null values
df_cleaned_rows = df.dropna()

# Remove columns with any null values (if needed)
df_cleaned = df_cleaned_rows.dropna(axis=1)

# Save the cleaned DataFrame to a new CSV file
cleaned_csv_file_path = 'cleaned_file.csv'  # Replace with your desired output file path
df_cleaned.to_csv(cleaned_csv_file_path, index=False)

# Check if there are any null values left
if not df_cleaned.isnull().values.any():
    print("No null values found in the cleaned DataFrame.")
else:
    print("There are still null values in the cleaned DataFrame.")
