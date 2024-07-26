# In this file we are going filter the data we need and write them into a new file. 
import numpy as np
import pandas as pd

import sys

# table_schema = types.StructType([
#     types.StructField('Course', types.StringType()),
#     types.StructField('Course Number', types.StringType()),
#     types.StructField('2019-02', types.IntegerType()),
#     types.StructField('2019-03', types.IntegerType()),
#     types.StructField('2020-01', types.IntegerType()),
#     types.StructField('2020-02', types.IntegerType()),
#     types.StructField('2020-03', types.IntegerType()),
#     types.StructField('2021-01', types.IntegerType()),
#     types.StructField('2021-02', types.IntegerType()),
#     types.StructField('2021-03', types.IntegerType()),
#     types.StructField('2022-01', types.IntegerType()),
#     types.StructField('2022-02', types.IntegerType()),
#     types.StructField('2022-03', types.IntegerType()),
#     types.StructField('2023-01', types.IntegerType()),
#     types.StructField('2023-02', types.IntegerType()),
#     types.StructField('2023-03', types.IntegerType()),
#     types.StructField('2024-01', types.IntegerType()),
#     types.StructField('2024-02', types.IntegerType())

# ])


# def main(in_directory, out_directory):
def main():
    # Removing the first 6 rows, since that data isnt required.
    data = pd.read_excel(f'data/database.1194.xlsx', header=6)
    
    data = data.reset_index(drop=True)
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Kepping only the last date Enrolment Status as we dont need the prior date enrolment reports
    max_date = data['Date'].max()
    data = data[data['Date'] == max_date]
    
    # Keeping only the columns we need
    data = data[['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'ActEnrol', 'Location']]
    
    print(data)

if __name__=='__main__':
    # in_directory = sys.argv[1]
    # out_directory = sys.argv[2]
    # main(in_directory, out_directory)
    main()