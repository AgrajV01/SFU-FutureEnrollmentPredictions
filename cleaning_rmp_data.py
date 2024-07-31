# Title: Course Enrolment Predictions 
# Author 1: Md Rownak Abtahee Diganta (Student ID: 301539632)
# Author 2: Agraj Vuppula (Student ID: 301538406)
# Author 3: Gowtam Krishnan Garapati (Student ID: 301596729)

# This code is for cleaning the extracted data file we got by web scrapping from Ratemyprof.
# After cleaning data this will save the cleaned data as a csv file. 

import pandas as pd

# Load the CSV file
file_path = 'professor_ratings_all.csv'
df = pd.read_csv(file_path)

# Drop rows where the 'Quality' column has no value
df_cleaned = df.dropna(subset=['Quality'])

# Drop duplicate rows based on the 'Professor_Name' column, keeping the first occurrence
df_deduplicated = df_cleaned.drop_duplicates(subset='Professor_Name', keep='first')

# Save the cleaned and deduplicated dataframe to a new CSV file
output_path = 'cleaned_professor_ratings_data.csv'
df_deduplicated.to_csv(output_path, index=False)

print("Rows with missing 'Quality' values removed and duplicates handled. File saved to:", output_path)
