# ✈️ Flight Fare Prediction | Machine Learning, Flask & Docker Deployment

A Machine Learning web application that predicts flight ticket prices based on flight details such as airline, source, destination, number of stops, journey date, and flight duration.

The project uses **XGBoost Regression** as the final prediction model and is deployed as a Flask web application inside a Docker container.

---

## Project Overview

This project focuses on predicting flight ticket prices using Machine Learning techniques. The model analyzes flight-related characteristics such as airline, source, destination, number of stops, journey date, and flight duration to estimate the expected flight fare.

The project demonstrates a complete Machine Learning workflow, including data preprocessing, exploratory data analysis, feature engineering, model building, evaluation, model comparison, and deployment using Flask and Docker.

---

## 🎯 Objectives

* Analyze and understand the flight fare dataset.
* Perform data cleaning and preprocessing.
* Conduct Exploratory Data Analysis (EDA).
* Engineer useful flight-related features.
* Encode categorical variables.
* Build regression models for flight fare prediction.
* Compare model performance using evaluation metrics.
* Select the best-performing Machine Learning model.
* Save the trained model and preprocessing objects.
* Build a Flask-based prediction web application.
* Containerize the application using Docker.
* Deploy the application as a live web service.

---

## 🔄 Project Workflow

Data Collection → Data Cleaning → Exploratory Data Analysis → Feature Engineering → Categorical Encoding → Train-Test Split → Feature Scaling → Model Building → Model Evaluation → Model Selection → Flask Application → Docker Deployment

---

## 📊 Dataset Information

The project uses historical flight fare data containing information about different flights and their corresponding ticket prices.

The dataset includes flight details such as:

| Feature | Description |
|---|---|
| Airline | Airline operating the flight |
| Source | Flight departure city |
| Destination | Flight arrival city |
| Route | Flight route |
| Dep_Time | Departure time |
| Arrival_Time | Arrival time |
| Duration | Total flight duration |
| Total_Stops | Number of stops during the journey |
| Additional_Info | Additional flight information |
| Journey_Day | Day of the journey |
| Journey_Month | Month of the journey |
| Price | Flight ticket price / Target Variable |

---

## 🔍 Exploratory Data Analysis

The following analyses were performed:

### Univariate Analysis

* Flight Fare Distribution
* Airline Distribution
* Number of Stops Distribution
* Journey Month Distribution
* Journey Day Distribution
* Flight Duration Analysis

### Bivariate Analysis

* Airline vs Flight Fare
* Total Stops vs Flight Fare
* Journey Month vs Flight Fare
* Source vs Flight Fare
* Destination vs Flight Fare
* Flight Duration vs Flight Fare

### Multivariate Analysis

* Correlation Analysis
* Feature Relationship Exploration
* Airline and Route Analysis
* Flight Duration Analysis
* Feature Importance Analysis

---

## ⚙️ Feature Engineering

The following preprocessing and feature engineering techniques were applied:

* Extracted journey day from the journey date.
* Extracted journey month from the journey date.
* Converted flight duration into numerical features.
* Created:
  * `Duration_hours`
  * `Duration_minutes`
* Converted categorical variables into numerical representations using one-hot encoding.
* Encoded airline information.
* Encoded source cities.
* Encoded destination cities.
* Converted number of stops into numerical values.
* Applied feature scaling where required.

## 🤖 Models Used

### 1. Linear Regression

* Used as the baseline regression model.
* Provides a simple benchmark for flight fare prediction.

### 2. Ridge Regression

* Used as a regularized linear regression model.
* Helps handle multicollinearity among the input features.

### 3. Random Forest Regressor

* Used to capture non-linear relationships between flight characteristics and ticket prices.
* Provides an ensemble-based regression approach.

### 4. XGBoost Regressor

* Used to capture complex non-linear relationships between flight features and ticket prices.
* Achieved the best performance among all evaluated models.
* Selected as the final deployment model.

### 5. Artificial Neural Network (ANN)

* Used as an additional deep learning regression approach.
* Evaluated against traditional Machine Learning models.

---

## 📈 Model Performance

The models were evaluated using **RMSE** and **R² Score**.

| Model | RMSE | R² Score |
|---|---:|---:|
| Linear Regression | 2866.90 | 0.6188 |
| Ridge Regression | 2866.90 | 0.6188 |
| Random Forest | 2268.31 | 0.7614 |
| **XGBoost** | **1915.85** | **0.8298** |
| ANN | 2633.72 | 0.6783 |

---

## 🏆 Best Model

The **XGBoost Regressor** was selected as the final deployment model.

### XGBoost Performance

* **RMSE:** 1915.85
* **R² Score:** 0.8298
* **Problem Type:** Regression
* **Target Variable:** Flight Fare / Price

XGBoost achieved the **lowest RMSE** and the **highest R² Score** among all evaluated models, making it the best-performing model for this project.

XGBoost provides a tree-based gradient boosting approach and supports regression through its `XGBRegressor` interface.

---

## 📊 Key Insights

* ✈️ **Airline** has an important influence on flight ticket prices.
* 🔄 The **number of stops** can significantly affect the fare.
* 📍 **Source and destination** cities contribute to differences in flight pricing.
* ⏱️ **Flight duration** provides useful information for predicting ticket prices.
* 📅 **Journey day and month** can influence fare variations.
* 🛫 Different flight routes can have significantly different price ranges.
* 🤖 XGBoost performed better than the other evaluated models by capturing non-linear relationships between flight features and ticket prices.
* 📈 Machine Learning can be used as a useful tool for estimating expected flight fares from historical flight information.

---

## 💼 Business Recommendations

* Use flight fare prediction to help travelers estimate expected ticket prices.
* Travel platforms can provide predicted fare ranges to support booking decisions.
* Travel agencies can use predictive analytics to identify pricing patterns.
* Airlines can analyze historical flight characteristics to support pricing analysis.
* Use route, airline, duration, and stop information together for better fare analysis.
* Integrate real-time flight information to improve prediction accuracy.
* Develop price-alert functionality to notify users when predicted fares are relatively lower.
* Combine Machine Learning predictions with historical pricing trends for better travel planning.

---

---

## 🚀 Live Demo

[![Open Live Demo](https://img.shields.io/badge/🚀%20Open%20Live%20Demo-Flight%20Fare%20Prediction-brightgreen?style=for-the-badge)](https://flight-fare-prediction-th4x.onrender.com/)

## 💻 Source Code

[![GitHub Repository](https://img.shields.io/badge/💻%20View%20Source%20Code-GitHub-black?style=for-the-badge)](https://github.com/khushigithub1/flight-fare-prediction)
---


## 🛠️ Technologies Used

### Programming

* Python 3.11

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* XGBoost
* TensorFlow / Keras

### Web Development

* Flask
* HTML5
* CSS3

### Deployment & Tools

* Docker
* Git
* GitHub
* Jupyter Notebook

---

## 🚀 Future Improvements

* Real-time flight fare data integration
* Advanced feature engineering
* Hyperparameter tuning for improved model performance
* Airline-specific fare prediction
* Interactive flight analytics dashboard
* Flight fare comparison functionality
* Historical price trend visualization
* Prediction history
* Price alert and notification system
* Automated model retraining
* CI/CD pipeline
* Cloud monitoring
* Custom domain integration
* Integration with live flight APIs

---

## 📬 Connect With Me

* **LinkedIn:** https://www.linkedin.com/in/akanksha-srivastava-20a43623
* **GitHub:** https://github.com/khushigithub1

---

## 👩‍💻 Author

### Akanksha Srivastava

**Data Science & Machine Learning Enthusiast**

Passionate about building practical Machine Learning solutions, predictive applications, and deploying data-driven projects as real-world web applications.

