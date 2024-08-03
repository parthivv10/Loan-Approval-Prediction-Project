import streamlit as st
import pandas as pd
import pickle as pk

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

model = pk.load(open('model.pkl', 'rb'))
scaler = pk.load(open('scaler.pkl', 'rb'))
st.markdown('<div class="title">Online Loan Approval Prediction</div>', unsafe_allow_html=True)
st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown('## About Us')
st.markdown('This Loan Predictor website is designed to help users assess their loan eligibility based on various parameters. Using advanced machine learning models, we provide accurate predictions to assist users in their financial planning.At Online Loan Approval Prediction website, our mission is to empower individuals with the information they need to make informed financial decisions. We understand that the loan application process can be daunting, and our goal is to simplify this experience by providing accurate and instant predictions on loan eligibility.')

st.markdown('<br><br>', unsafe_allow_html=True)
grad = st.selectbox('Choose your Education status', ['Graduated', 'Not Graduated'])
no_of_dep = st.slider('Choose No of dependents', 0, 5)
Loan_Amount = st.text_input('Enter your required Loan Amount', '0')
self_emp = st.selectbox('Employment Status', ['Yes', 'No'])
Cibil = st.text_input('Enter your Cibil Score', '0')
Annual_Income = st.text_input('Enter your Annual Income', '0')
Loan_Dur = st.text_input('Enter Loan Duration required(in years)', '0')
Assets = st.text_input('Enter your Assets worth', '0')

no_of_dep = int(no_of_dep)
Annual_Income = float(Annual_Income)
Loan_Amount = float(Loan_Amount)
Loan_Dur = int(Loan_Dur)
Cibil = int(Cibil)
Assets = float(Assets)

if grad == 'Graduated':
    grad_s = 0
else:
    grad_s = 1

if self_emp == 'No':
    emp_s = 0
else:
    emp_s = 1

if st.button("Predict"):
    pred_data = pd.DataFrame([[no_of_dep, grad_s, emp_s, Annual_Income, Loan_Amount, Loan_Dur, Cibil, Assets]],
                             columns=['no_of_dependents', 'education', 'self_employed', 'income_annum', 'loan_amount', 'loan_term', 'cibil_score', 'Assets'])
    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)
    if predict[0] == 1:
        st.markdown('<div class="loan-approved">Congrats,Loan is approved</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="loan-rejected">Sorry,Loan is rejected</div>', unsafe_allow_html=True)


st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown('## Our Vision')
st.markdown('We envision a world where financial transparency and accessibility are available to everyone. By leveraging technology and data, we strive to make the loan application process more transparent, efficient, and fair. We aim to be a trusted partner in your financial journey, providing insights and tools that help you achieve your financial goals.')
st.markdown('## Contact Us')
st.markdown('If you have any questions, feedback, or need assistance, our customer support team is here to help. You can reach us at parthiv.1609@gmail.com . We value your input and are always looking for ways to improve our service.')
