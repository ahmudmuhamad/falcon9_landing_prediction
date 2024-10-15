# Falcon 9 Landing Prediction Project

Falcon 9 successful landing:
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/landing_1.gif)


![Unsuccessful Landing](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/crash.gif)

## Project Overview

This project aims to predict the success of Falcon 9 landings using historical launch data. The process involved several key steps, including web scraping, exploratory data analysis (EDA), training label determination, geographical analysis, machine learning model development, and deployment of the predictive model using a Streamlit application.

## Project Steps

### 1. Web Scraping Falcon 9 and Falcon Heavy Launch Records

The initial step involved scraping launch records for Falcon 9 and Falcon Heavy rockets from Wikipedia. This data included critical information about each launch, such as launch dates, rocket versions, payload masses, and outcomes. The web scraping was performed using Python libraries such as Beautiful Soup and Requests, enabling efficient extraction of structured data from the HTML content of the Wikipedia pages.

### 2. Exploratory Data Analysis (EDA)

After gathering the data, comprehensive exploratory data analysis was conducted to understand the dataset's characteristics. This included:

- **Data Cleaning**: Handling missing values, correcting data types, and removing duplicates.
- **Data Visualization**: Utilizing libraries like Matplotlib and Seaborn to create visualizations that highlighted trends and distributions within the dataset.
- **Feature Analysis**: Examining individual features and their relationships to determine which factors might influence landing success.

#### Determine Training Labels

During the EDA phase, training labels for the machine learning models were established based on the outcomes of the launches. This involved categorizing outcomes into successful and unsuccessful landings, providing a clear target variable for model training.

### 3. Launch Sites Location Analysis with Folium

To enhance the geographical understanding of launch sites, Folium was used to create interactive maps. This analysis provided insights into the locations of Falcon 9 launches, highlighting the proximity of each launch site to populated areas and other geographical landmarks. The interactive maps facilitated a better understanding of the spatial distribution of the launches.

### 4. Machine Learning Model Development

The core of the project involved developing several machine learning models to predict landing outcomes. The following algorithms were implemented:

- **Logistic Regression**: A foundational model used for binary classification, providing a baseline for performance evaluation.
- **Support Vector Machine (SVM)**: A more complex model that aims to find the optimal hyperplane for classification.
- **K-Nearest Neighbors (KNN)**: A non-parametric method that classifies instances based on the majority label of their nearest neighbors.
- **Decision Tree**: A model that makes decisions based on a series of feature-based splits, useful for understanding feature importance.

Each model was evaluated using metrics such as accuracy, F1 score, and Jaccard score to determine the best-performing model for the task.

### 5. Model Deployment Using Streamlit

The final step involved deploying the selected machine learning model using a Streamlit application. This interactive web app allows users to input launch parameters and receive real-time predictions regarding the likelihood of a successful landing. The app was developed to provide a user-friendly interface, enhancing accessibility for users interested in Falcon 9 landing predictions.

## Conclusion

This project demonstrates a comprehensive approach to predictive modeling, from data collection and analysis to machine learning and deployment. The combination of web scraping, EDA, geographical analysis, and model development provides valuable insights into Falcon 9 landing outcomes and showcases the potential for further exploration and enhancement in rocket launch success prediction.
