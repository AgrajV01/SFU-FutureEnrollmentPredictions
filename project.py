# Title: Course Enrolment Predictions 
# Author 1: Md Rownak Abtahee Diganta (Student ID: 301539632)
# Author 2: Agraj Vuppula (Student ID: 301538406)
# Author 3: Gowtam Krishnan Garapati (Student ID: 301596729)

# All the imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score


def firstSteps():
    # Reading Data Files
    actual_data = pd.read_csv('ActualEnrolDataFile.csv')
    capacity_data = pd.read_csv('MaxEnrolDataFile.csv')
    # Load the professor ratings and course diggers data
    rateMyProfData = pd.read_csv('data/cleaned_professor_ratings_data.csv')
    courseDiggersData = pd.read_csv('data/courseDiggers.csv')

    # Replace NaN Values with Zeros values
    # Ref: https://www.geeksforgeeks.org/replace-nan-values-with-zeros-in-pandas-dataframe/ (Gained Knowledge)
    actual_data = actual_data.fillna(0)
    capacity_data = capacity_data.fillna(0)

    # Reorganizing data frames
    # ref: https://pandas.pydata.org/docs/reference/api/pandas.melt.html (Gained Knowledge)
    actual_data = pd.melt(
        actual_data,
        id_vars=['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location'],
        var_name='Term',
        value_name='Enrollment'
    )
    capacity_data = pd.melt(
        capacity_data,
        id_vars=['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location'],
        var_name='Term',
        value_name='Max Capacity'
    )

    # Merge the reorganized data frames
    # ref: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html (Gained Knowledge)
    data = actual_data.merge(
        capacity_data,
        how='outer',
        on=['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location', 'Term']
    )
    # print(data)
    semName = ['Summer 2019', 'Fall 2019', 'Spring 2020', 'Summer 2020', 'Fall 2020', 'Spring 2021', 'Summer 2021',
               'Fall 2021', 'Spring 2022', 'Summer 2022', 'Fall 2022', 'Spring 2023', 'Summer 2023', 'Fall 2023',
               'Spring 2024', 'Summer 2024', 'Fall 2024']
    data['Term'] = pd.Categorical(data['Term'], categories=semName, ordered=True)
    # print(data)
    return data, courseDiggersData, rateMyProfData

# Helper function
def courseUtlization(group):
        group = group.dropna(subset=['Enrollment', 'Max Capacity'])
        if len(group) == 0:
            return np.nan
        temp = group['Enrollment'] / group['Max Capacity']
        return np.mean(temp)
    
# Function for predicting future enrollment
def predicting_future_enrollment(data):
    # refernce links: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html
    # https://www.geeksforgeeks.org/python-coefficient-of-determination-r2-score/
    all_y_valid = []
    all_y_pred = []

    def knn_prediction(group):
        group = group.dropna(subset=['Enrollment'])
        # If a course has less than 3 records, then retun Nan
        if len(group) < 3:
            return pd.Series([np.nan, np.nan, np.nan], index=['Next Fall', 'Next Spring', 'Next Summer'])

        #  should change
        X = np.arange(len(group)).reshape(-1, 1)
        y = group['Enrollment'].values

        # Split the data into training and validation sets
        X_train, X_valid, y_train, y_valid = train_test_split(X, y)

        # Train KNN regressor
        model = make_pipeline(
            StandardScaler(),
            # KNeighborsRegressor(n_neighbors= min(3, len(group)))
            KNeighborsRegressor(n_neighbors=3))

        model.fit(X_train, y_train)
        # Validate the model on the validation set
        y_pred = model.predict(X_valid)

        # Accumulate the actual and predicted values
        all_y_valid.extend(y_valid)
        all_y_pred.extend(y_pred)

        # Predict next 3 terms
        future_X = np.array([[len(group)], [len(group) + 1], [len(group) + 2]])
        future_predictions = model.predict(future_X)
        return pd.Series(future_predictions, index=['Next Fall', 'Next Spring', 'Next Summer'])

    predictions = data.groupby(['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location']).apply(knn_prediction)

    # to print the avergae scores
    overall_r2_score = r2_score(all_y_valid, all_y_pred)
    print(f'Overall R² score: {overall_r2_score}')

    return predictions


def enrollment_trend_analysis(data):
    print("1: Check the Overall Enrollment trend")
    print("2: Check Enrollment trend of a specific course")
    choice1 = int(input("\nSelect between 1 or 2: "))

    if (choice1 == 1):
        trend = data.pivot(index=['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location'], columns='Term',
                           values='Enrollment').mean()
        trend.plot(kind='line', title='Overall Enrollment Trend Analysis')
        plt.xticks(ticks=range(len(trend.index)), labels=trend.index, rotation=35) 
        plt.xlabel('Term')
        plt.ylabel('Average Enrollment')
        plt.show()
    elif (choice1 == 2):
        choice2 = input("\nEnter the Subject and CatNbr(Example CMPT 353): ")
        subject, catNbr = choice2.split()

        temp = data[(data['Subject'] == subject) & (data['CatNbr'] == catNbr)]
        grouped = temp.groupby(['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location'])

        for name, group in grouped:
            plt.figure(figsize=(15, 6))
            plt.plot(group['Term'], group['Enrollment'], marker='o')
            plt.title(f"Enrollment Trend for {name}")
            plt.xlabel("Term")
            plt.ylabel("Enrollment")
            plt.show()
    else:
        print("Wrong Input!!")
    
def identify_over_under_subscribed_courses(data):
    temp = data.groupby(['Subject', 'CatNbr', 'Course Title', 'Sect', 'Type', 'Location']).apply(courseUtlization)
    over_enrolled = temp[temp > 0.90]
    under_enrolled = temp[temp < 0.50]

    return over_enrolled, under_enrolled

def predict_high_demand_courses(data):
    choice = int(input("\nEnter the Minimum average number of students to consider a course high-demand: "))
    # high demand means that the average predicted enrollment is greater than the choice taken.
    temp = predicting_future_enrollment(data)
    high_demand = temp[temp.apply(lambda x: np.mean(x) > choice, axis=1)]
    return high_demand

def predict_low_demand_courses(data):
    choice = int(input("\nEnter the Maximim average number of students to consider a course low-demand: "))
    # low demand means that the average predicted enrollment is lower than the choice taken.
    temp = predicting_future_enrollment(data)
    low_demand = temp[temp.apply(lambda x: np.mean(x) < choice, axis=1)]
    return low_demand

def seasonal_enrollment_patterns(data):
    data['Season'] = data['Term'].str.split().str[0]
    temp = data.groupby('Season')['Enrollment'].mean().reindex(['Spring', 'Summer', 'Fall'])

    plt.figure(figsize=(10, 6))
    temp.plot(kind='bar', color='skyblue')
    plt.xlabel('Season')
    plt.ylabel('Average Enrollment')
    plt.title('Average Enrollment by Season')
    plt.show()

def recommend_courses_using_courseDiggers(course_data):
    easy_difficulty = 2
    easy_workload = 2
    # Strip spaces from column names and course names
    course_data.columns = course_data.columns.str.strip()
    # Filter courses based on difficulty and workload
    recommended_courses = course_data[(course_data['DIFFICULTY'] <= easy_difficulty) & (course_data['WORKLOAD'] <= easy_workload)]
    return recommended_courses

def recommend_professors_using_rateMyProf(professor_data, course_name):
    # Filter professors who have taught the specified course
    temp = professor_data[professor_data['Class_Name'] == course_name]
    if temp.empty:
        print(f"No professors found for the course: {course_name}")
        return None
    # Sort by quality rating in descending order
    temp = temp.sort_values(by='Quality', ascending=False)
    return temp

def main():
    data,courseDiggersData, rateMyProfData  = firstSteps()
    # User Interface

    print("\nWelcome to our data science software!! ")
    print("This software will help you to get a lot of important predictions and information regarding courses offered here in SFU.")
    print("This software will show you options and you need to choose the desired option to know that particular thing you want to know.")
    print("The options are given below.")
    flag = True  # To control the loops of the prompts
    while flag:
        print("\nChoose an analysis type:\n")
        print("1. Predicting Future Enrollment")
        print("2. Enrollment Trend Analysis")
        print("3. Identify Over/Under Subscribed Courses")
        print("4. Predict High-Demand Courses")
        print("5. Predict Low-Demand Courses")
        print("6. Seasonal Enrollment Patterns")
        print("7. Recommend Courses with Good Ratings")
        print("8. Recommend Professors for a Particular Course")
        print("9. Exit")
        try:
            choice = int(input("\nPlease enter a number from 1 to 9: "))
            if choice == 1:
                predictions = predicting_future_enrollment(data)
                print(predictions)
            elif choice == 2:
                enrollment_trend_analysis(data)
            elif choice == 3:
                over_subscribed, under_subscribed = identify_over_under_subscribed_courses(data)
                print("Over Subscribed Courses:", over_subscribed)
                print("Under Subscribed Courses:", under_subscribed)
            elif choice == 4:
                high_demand_courses = predict_high_demand_courses(data)
                print(high_demand_courses)
            elif choice == 5:
                low_demand_courses = predict_low_demand_courses(data)
                print(low_demand_courses)
            elif choice == 6:
                seasonal_enrollment_patterns(data)
            elif choice == 7:
                temp = recommend_courses_using_courseDiggers(courseDiggersData)
                print(temp)
            elif choice == 8:
                course = input("Please enter the course name(Example CMPT353): ")
                temp = recommend_professors_using_rateMyProf(rateMyProfData, course)
                print(temp)
            elif choice == 9:
                print("\nExiting the programme.")
                print("Thank you for using our software!! Hope that you had a nice experience. Have a good day!!!\n")
                flag = False  # Changing the flag to exit the code
            else:
                print("Invalid choice! Select between 1-7.")
        except ValueError:
            print("Wrong Input! Try Again!!")


if __name__ == '__main__':
    main()
