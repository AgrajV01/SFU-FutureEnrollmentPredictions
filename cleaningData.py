# In this file we are going filter the data we need and write them into a new file. 
# taken some reference from https://stackoverflow.com/questions/58295555/pandas-append-new-row-with-a-different-number-of-columns
import numpy as np
import pandas as pd

def cleanData(data):
    data['Date'] = pd.to_datetime(data['Date'])
        
    # Kepping only the last date Enrolment Status as we dont need the prior date enrolment reports
    max_date = data['Date'].max()
    data = data[data['Date'] == max_date]
    
    # Keeping only the columns we need
    data = data[['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'ActEnrol', 'Location']]
    return data
    
def main():
    
    dataFilesList = [
    'database.1194.xlsx','database.1197.xlsx', 'database.1201.xlsx', 'database.1204.xlsx', 'database.1207.xlsx', 
    'database.1211.xlsx', 'database.1214.xlsx', 'database.1217.xlsx', 'database.1221.xlsx', 
    'database.1224.xlsx', 'database.1227.xlsx', 'database.1231.xlsx', 'database.1234.xlsx', 
    'database.1237.xlsx', 'database.1241.xlsx', 'database.1244.xlsx', 'database.1247.xlsx']
    
    semName = ['Summer 2019','Fall 2019','Spring 2020','Summer 2020', 'Fall 2020', 'Spring 2021','Summer 2021', 'Fall 2021', 
        'Spring 2022','Summer 2022', 'Fall 2022','Spring 2023','Summer 2023', 'Fall 2023', 'Spring 2024','Summer 2024','Fall 2024']
    i =0
    dataFile =[]
    for file in dataFilesList:
        
        # Removing the first 6 rows, since that data isnt required.
        data = pd.read_excel(f'data/{file}', header=6)
        data = data.reset_index(drop=True)

        # only the last file, has the column header name with Section instead of Sect, so modifying according to that
        if file == 'database.1247.xlsx':
            data.rename(columns={'Section': 'Sect'}, inplace=True)
        
        data = cleanData(data)
        
        # Rename the ActEnrol column to the semester name
        data.rename(columns={'ActEnrol': semName[i]}, inplace=True)
        dataFile.append(data)
        i =i+1

    # print(dataFile)
    
    # finally create a new excel file with the cleaned data in it.
    finalDataFile = pd.concat(dataFile, ignore_index=True)
    finalDataFile = finalDataFile.groupby(['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location'], as_index=False).first()
    finalDataFile.to_excel('FinalDataFile.xlsx', index=False)
    
if __name__=='__main__':
    main()