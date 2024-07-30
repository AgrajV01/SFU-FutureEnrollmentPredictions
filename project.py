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
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Function for predicting future enrollment
def predicting_future_enrollment(data):
    def knn_prediction(group):
        group = group.dropna(subset=['Enrollment'])
        # If a course has less than 3 records, then retun Nan
        if len(group) < 3:
            return pd.Series([np.nan, np.nan, np.nan], index=['Next Fall', 'Next Spring', 'Next Summer'])
        
        X = np.arange(len(group)).reshape(-1, 1)
        y = group['Enrollment'].values
        
        # Train KNN regressor
        model = make_pipeline(
            StandardScaler(), 
            # KNeighborsRegressor(n_neighbors= min(3, len(group)))
            KNeighborsRegressor(n_neighbors= 3))
        model.fit(X, y)
        
        # Predict next 3 terms
        future_X = np.array([[len(group)], [len(group) + 1], [len(group) + 2]])
        future_predictions = model.predict(future_X)
        return pd.Series(future_predictions, index=['Next Fall', 'Next Spring', 'Next Summer'])
    predictions = data.groupby(['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location']).apply(knn_prediction)
    return predictions

def enrollment_trend_analysis(data):
    # Anna Fill
    print("Hello")

def identify_over_under_subscribed_courses(data):
    # Anna Fill 
    return data['Subject'],data['CatNbr']
    
def predict_high_demand_courses(data):
    # Anna Fill 
    return data

def predict_low_demand_courses(data):
    # Anna Fill 
    return data
    
def seasonal_enrollment_patterns(data):
    # Anna Fill 
    print("Hello")
    
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
    
    # User Interface  
    
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
        try:
            choice = int(input("\nPlease enter a number from 1 to 7: "))
            if choice == 1:
                print("You have chosen option 1.")
                predictions= predicting_future_enrollment(data)
                print(predictions)
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
                print("\nExiting the programme.")
                print("Thank you for using our software!! Hope that you had a nice experience. Have a good day!!!\n")
                flag = False # Changing the flag to exit the code
            else:
                print("Invalid choice! Select between 1-7.")
        except ValueError:
            print("Wrong Input! Try Again!!")   
            
if __name__ == '__main__':
    main()