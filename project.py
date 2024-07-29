# Title: Course Enrolment Predictions 
# Author 1: Md Rownak Abtahee Diganta (Student ID: 301539632)
# Author 2: Agraj Vuppula             (Student ID: 301538406)
# Author 3: gowtam Krishnan garapati  (Student ID: 301596729)

# All the imports 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Function for predicting future enrollment
def predicting_future_enrollment(data):
    # Anna Fill 

def enrollment_trend_analysis(data):
    # Anna Fill 

def identify_over_under_subscribed_courses(data):
    # Anna Fill 
    
def predict_high_demand_courses(data):
    # Anna Fill 

def predict_low_demand_courses(data):
    # Anna Fill 
    
def seasonal_enrollment_patterns(data):
    # Anna Fill 
    
def main():
    
    # Reading Data Files 
    actual_data = pd.read_csv('ActualEnrolDataFile.csv')
    capacity_data = pd.read_csv('MaxEnrolDataFile.csv')

    # Replace NaN Values with Zeros values
    # Ref: https://www.geeksforgeeks.org/replace-nan-values-with-zeros-in-pandas-dataframe/ (Gained Knowledge)
    actual_data = actual_data.fillna(0)
    #print(actual_data)
    capacity_data = capacity_data.fillna(0)
    #print(capacity_data)

    # Reorganizing data frames 
    # ref: https://pandas.pydata.org/docs/reference/api/pandas.melt.html (Gained Knowledge)
    
    actual_data = pd.melt(
        actual_data,
        id_vars=['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location'],
        var_name='Term',
        value_name='Enrollment'
    )
    #print(actual_data)
    capacity_data = pd.melt(
        capacity_data,
        id_vars=['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location'],
        var_name='Term',
        value_name='Max Capacity'
    )
    #print(actual_data)
    # Merge the reorganized data frames
    # ref: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html (Gained Knowledge)
    
    data = actual_data.merge(
        capacity_data, 
        how='outer',
        on=['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location', 'Term']
        
    )
    #print(data)
    
    # knn 
    grouped_data = data.groupby(['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location'])
    print(grouped_data)
    
    # User Interface in Terminal 
    
    print("Welcome to our data science software!! \n")
    print("This software will help you to get a lot of important predictions and information regarding courses offered here in SFU.\n")
    print("This software will show you options and you need to choose the desired option to know that particular thing you want to know.\n")
    print("The options are given below.\n")
    flag = True # To control the loops of the prompts 
    while flag:
        print("\nChoose an analysis type:\n")
        print("1. Predicting Future Enrollment")
        print("2. Enrollment Trend Analysis")
        print("3. Identify Over/Under Subscribed Courses")
        print("4. Predict High-Demand Courses")
        print("5. Predict Low-Demand Courses")
        print("6. Seasonal Enrollment Patterns")
        print("7. Exit")
        print("\nPlease enter a number from 1 to 7.\n")
        try:
            
            choice = int(input("Enter the number of your choice: "))
            print("\n")

            if choice == 1:
                print("You have chosen option 1.")
                predict_data= predicting_future_enrollment(data)
                #print(predictions)
            elif choice == 2:
                print("You have chosen option 2.")
                enrollment_trend_analysis(data)
            elif choice == 3:
                print("You have chosen option 3.")
                over_subscribed, under_subscribed = identify_over_under_subscribed_courses(data)
                print("Over Subscribed Courses:", over_subscribed)
                print("Under Subscribed Courses:", under_subscribed)
            elif choice == 4:
                print("You have chosen option 4.")
                high_demand_courses = predict_high_demand_courses(data)
                print(high_demand_courses)
            elif choice == 5:
                print("You have chosen option 5.")
                low_demand_courses = predict_low_demand_courses(data)
                print(low_demand_courses)
            elif choice == 6:
                print("You have chosen option 6.")
                seasonal_enrollment_patterns(data)
            elif choice == 7:
                print("\nYou have chosen option 7.")
                print("\nExiting the programme. \n")
                print("Thank you for using our software!! Hope that you had a nice experience. Have a good day!!!")
                flag = False # Changing the flag to exit the code
                
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("You have entered a value which is not integer. Please enter a number from 1 to 7.")   
            
if __name__ == '__main__':
    main()