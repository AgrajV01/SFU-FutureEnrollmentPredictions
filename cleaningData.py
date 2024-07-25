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


def main(in_directory, out_directory):

    # file = pd.read_csv(in_directory, schema=table_schema)

    print("Initial commit")

    # cleaned_data.write.json(out_directory, compression='gzip', mode='overwrite')

if __name__=='__main__':
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]
    main(in_directory, out_directory)