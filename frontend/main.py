import streamlit as st
import requests

# Define backend URL
backend_url = 'http://127.0.0.1:8000'

st.set_page_config(
    page_title='Predict Page',
    page_icon='🤖',
    layout='wide'
)

# Display form and handle inputs
def display_form():
    st.title('Sepsis Predictor')

    with st.form('input_features'):
        st.header('Input Sepsis Features')

        col1, col2 = st.columns(2)

        with col1:
            Plasma_Glucose = st.number_input('Plasma_Glucose', min_value=0, step=1)
            Blood_Work_Result_1 = st.number_input('Blood_Work_Result_1', min_value=0, step=1)
            Blood_Pressure = st.number_input('Blood_Pressure', min_value=0, step=1)
            Blood_Work_Result_2 = st.number_input('Blood_Work_Result_2', min_value=0, step=1)
            Blood_Work_Result_3 = st.number_input('Blood_Work_Result_3', min_value=0, step=1)

        with col2:
            Body_Mass_Index = st.number_input('Body_Mass_Index', min_value=0.0, step=0.1)
            Blood_Work_Result_4 = st.number_input('Blood_Work_Result_4', min_value=0.0, step=0.1)
            Age = st.number_input('Age', min_value=0, step=1)
            Insurance = st.number_input('Insurance', min_value=0, max_value=1, step=1)

        # Form submission
        submitted = st.form_submit_button('Submit')

    return submitted, {
        'Plasma_Glucose': Plasma_Glucose,
        'Blood_Work_Result_1': Blood_Work_Result_1,
        'Blood_Pressure': Blood_Pressure,
        'Blood_Work_Result_2': Blood_Work_Result_2,
        'Blood_Work_Result_3': Blood_Work_Result_3,
        'Body_Mass_Index': Body_Mass_Index,
        'Blood_Work_Result_4': Blood_Work_Result_4,
        'Age': Age,
        'Insurance': Insurance,
    }

# Display results
def display_results(input_data):
    # Send requests to the FastAPI backend
    response_xgb = requests.post(f'{backend_url}/predict_sepsis/xgb_classifier', json=input_data)
    response_gb = requests.post(f'{backend_url}/predict_sepsis/gradient_boost', json=input_data)

    # Display the prediction results
    if response_xgb.status_code == 200 and response_gb.status_code == 200:
        prediction_xgb = response_xgb.json()['prediction']
        prediction_gb = response_gb.json()['prediction']
        st.success(f'Predicted Sepsis risk (XGB Classifier): {prediction_xgb}')
        st.success(f'Predicted Sepsis risk (Gradient Boosting Classifier): {prediction_gb}')
    else:
        if response_xgb.status_code != 200:
            st.error(f"XGB Classifier Error: {response_xgb.json()['detail']}")
        if response_gb.status_code != 200:
            st.error(f"Gradient Boosting Classifier Error: {response_gb.json()['detail']}")

if __name__ == '__main__':
    submitted, input_data = display_form()
    if submitted:
        display_results(input_data)

