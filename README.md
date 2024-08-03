# Loan-Approval-Prediction-Project
Project Description
This project aims to build a predictive model that can help financial institutions automate and enhance their loan approval process. By leveraging historical data, the model predicts the likelihood of loan approval based on various attributes of the loan applicants.

Key Steps and Results:
Data Collection and Preprocessing
Data Collection: Gathered historical data of loan applicants.
Data Cleaning: Handled missing values and inconsistencies in the dataset.
Feature Engineering: Encoded categorical variables and scaled numerical features.

Model Development:
Model Selection: Evaluated multiple machine learning algorithms including Logistic Regression, Decision Trees, Random Forest, Gradient Boosting, and Support Vector Machines (SVM).


Results:
The Random Forest Classifier outperformed other models with high accuracy and reliability.
The model demonstrated strong predictive power, making it a valuable tool for automating the loan approval process.

How to Run the App:

  Prerequisites
  Ensure you have the following installed:
    Python 3.x
    Jupyter Notebook
    Streamlit
  Installation
    Install the required Python libraries using the following command:
      pip install pandas numpy scikit-learn matplotlib seaborn streamlit
      Running the Jupyter Notebook
      Open Loan_Approval_Pred_Model.ipynb in Jupyter Notebook to explore the data preprocessing, model training, and evaluation steps.
      Running the Streamlit Application
        Navigate to the directory containing app.py.
      Run the following command to start the Streamlit web application:
        streamlit run app.py
The web application will launch in your default web browser. Enter the applicant details to get a loan approval prediction.
