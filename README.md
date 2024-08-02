# SFU Course Enrollment Predictions and Analysis Using RateMyProfessor Data

## Description

This project focuses on predicting the number of course sections needed based on enrollment trends and student preferences. It aims to optimize resource allocation and scheduling to accommodate student demand effectively.

## SFU Dataset

- **Course section availability**: https://www.sfu.ca/irp/courses/CourseSectionAvailabilityReport.html
- **Enrolment Registration reports**: https://www.sfu.ca/irp/enrolments.html
- **Course Diggers**: https://coursediggers.com/pages/explore
- **Rate My Professors**: https://www.ratemyprofessors.com/search/professors/1482?q=*

## Understanding the Problem

Universities face the challenge of efficiently scheduling courses to meet student demand while balancing resource constraints such as faculty availability and classroom space. Predicting the number of course sections needed helps in planning and allocating these resources effectively.

## Data Collection and Preparation

- **Data Source**: The project typically uses historical enrollment data provided by the university. This data includes information such as course offerings and enrollment numbers per section.
- **Data Cleaning and Integration**: The collected data needs to be cleaned to remove inconsistencies and errors.

## Benefits and Impact

- **Optimized Student Experience**: Ensuring that students have access to the courses they need, reducing scheduling conflicts, and improving graduation rates by minimizing delays caused by unavailable courses.
- **Efficiency in Resource Allocation**: Maximizing the utilization of faculty and classroom resources, potentially reducing costs associated with underutilized resources.
- **Strategic Planning**: Supporting long-term strategic planning by providing insights into evolving student demand trends and areas of growth or decline in enrollment.

In conclusion, predicting course section requirements for student enrollment is a data-driven approach to optimizing university operations and enhancing the student experience. By leveraging advanced analytics and machine learning, universities can make informed decisions that align with both student needs and institutional goals.

## Resources Summary Names

### 2024/25 Reports
- 1247 (Fall)
- 1244 (Summer)

### 2023/24 Reports
- 1241 (Spring)
- 1237 (Fall)
- 1234 (Summer)

### 2022/23 Reports
- 1231 (Spring)
- 1227 (Fall)
- 1224 (Summer)

### 2021/22 Reports
- 1221 (Spring)
- 1217 (Fall)
- 1214 (Summer)

### 2020/21 Reports
- 1211 (Spring)
- 1207 (Fall)
- 1204 (Summer)

### 2019/20 Reports
- 1201 (Spring)
- 1197 (Fall)
- 1194 (Summer)

## Course Enrollment Predictions

### Authors:
- Md Rownak Abtahee Diganta (Student ID: 301539632)
- Agraj Vuppula (Student ID: 301538406)
- Gowtam Krishnan Garapati (Student ID: 301596729)

## Overview

This project aims to predict future course enrollments, analyze enrollment trends, identify over/under subscribed courses, predict high/low demand courses, and recommend courses and professors based on ratings. The project uses historical enrollment data and professor ratings to make these predictions.

## Project Structure

- **data/**: Directory containing all the data files used in the project.
- **ActualEnrolDataFile.csv**: Processed file containing actual enrollment data.
- **MaxEnrolDataFile.csv**: Processed file containing maximum enrollment data.
- **new_professor_ratings_all.csv**: Processed file containing professor ratings data.
- **project.py**: Main script to run the course enrollment prediction software.
- **cleaningData.py**: Script to clean the raw enrollment data.
- **rmp_data.py**: Script to extract professor ratings from RateMyProfessor using web scraping.
- **README.md**: This file.

## Dependencies

To run this project, you need the following libraries:
- pandas
- numpy
- matplotlib
- scikit-learn
- BeautifulSoup
- requests
- selenium
- webdriver_manager

You can install these dependencies using pip:


## Data Files

The following data files are required:
- `ActualEnrolDataFile.csv`: Contains the actual enrollment data.
- `MaxEnrolDataFile.csv`: Contains the maximum enrollment data.
- `new_professor_ratings_all.csv`: Contains the professor ratings data.
- `courseDiggers.csv`: Contains the course ratings data
- Other Excel files in the data directory are used for raw data processing.

## Scripts

### project.py

This is the main script that provides a user interface to select different analysis types. To run this script, use the command:
python3 project.py


### cleaningData.py

This script processes raw enrollment data from multiple Excel files and creates two CSV files: `ActualEnrolDataFile.csv` and `MaxEnrolDataFile.csv`. 


### rmp_data.py

This script uses web scraping to extract professor ratings from RateMyProfessor and saves the data into `new_professor_ratings_all.csv`. To run this script, use the command:
python3 rmp_data.py
You can update the link https://www.ratemyprofessors.com/search/professors/1482?q=* in the rmp_data.py to get the professors rating data of another university.


## Functionality of the project.py

### Predicting Future Enrollment

- Predict future course enrollments using historical data. It uses KNN regression to make predictions.

### Enrollment Trend Analysis

- Analyze overall enrollment trends or trends for a specific course over different terms.

### Identify Over/Under Subscribed Courses

- Identify courses that are over or under subscribed based on their enrollment and maximum capacity.

### Predict High-Demand Courses

- Predict courses that will have high demand in future terms based on average predicted enrollment.

### Predict Low-Demand Courses

- Predict courses that will have low demand in future terms based on average predicted enrollment.

### Seasonal Enrollment Patterns

- Analyze average enrollment by season (Spring, Summer, Fall).

### Recommend Courses with Good Ratings

- Recommend courses based on low difficulty and workload using the CourseDiggers data.

### Recommend Professors for a Particular Course

- Recommend the best professor for a particular course based on quality and difficulty ratings from RateMyProfessor.

## Usage

1. Clone the repository:

   git clone https://github.sfu.ca/gkg32/cmpt353_sfu_course_section_prediction

   cd your-repo-directory 


2. Ensure all data files are in the `data` directory.

3. Run the project.py script using python3 project.py command

4. Follow the on-screen prompts to select an analysis type and get the desired information.

## Notes

- Ensure your data files are correctly formatted and located in the appropriate directories.
- Adjust file paths in the scripts if necessary to match your directory structure.

