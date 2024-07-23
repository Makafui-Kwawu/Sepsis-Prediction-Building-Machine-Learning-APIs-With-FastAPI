import streamlit as st
import requests

st.set_page_config(
    page_title="Sepsis Prediction Page",
    page_icon="🤖",
    layout="wide"
)

# Set title of the application
st.title("Sepsis Predict-Pro 🤖")

# Load the API endpoints
xgb_endpoint = "http://127.0.0.1:8000/predict_sepsis/xgb_classifier"
gradient_boost_endpoint = "http://127.0.0.1:8000/predict_sepsis/gradient_boost"

# Initialize model selection session state
if "model_select" not in st.session_state:
    st.session_state["model_select"] = "XGB Classifier"

# Select between the two endpoints of the ML model
col1, col2 = st.columns(2)
with col2:
    st.selectbox("Model Selection", options=["XGB Classifier", "Gradient Boost"], key="model_select")

# Initialize session state for input features
input_keys = ["Plasma_Glucose", "Blood_Work_Result_1", "Blood_Pressure", "Blood_Work_Result_2",
              "Blood_Work_Result_3", "Body_Mass_Index", "Blood_Work_Result_4", "Age", "Insurance"]
for key in input_keys:
    if key not in st.session_state:
        st.session_state[key] = 0

# Define function to accept inputs and display forms
def display_forms():
    with st.form("input-features"):
        col1, col2 = st.columns(2)
        with col1:
            st.write('### Patient Demographics')
            st.number_input("Age", min_value=0, step=1, key="Age")
            st.number_input("Insurance", min_value=0, max_value=1, step=1, key="Insurance")

            st.write('### Vital Signs')
            st.number_input("Blood Pressure", min_value=0, step=1, key="Blood_Pressure")
            st.number_input("Body Mass Index", min_value=0.0, step=0.1, key="Body_Mass_Index")
            
        with col2:
            st.write('### Blood Works')
            st.number_input("Blood Work Result 1", min_value=0, step=1, key="Blood_Work_Result_1")
            st.number_input("Blood Work Result 2", min_value=0, step=1, key="Blood_Work_Result_2")
            st.number_input("Blood Work Result 3", min_value=0, step=1, key="Blood_Work_Result_3") 
            st.number_input("Blood Work Result 4", min_value=0.0, step=0.1, key="Blood_Work_Result_4")
            st.number_input("Plasma Glucose", min_value=0, step=1, key="Plasma_Glucose")
        
        submit_button = st.form_submit_button("Predict")
    return submit_button

# Define function to make predictions
def make_prediction():
    input_features = {key: st.session_state[key] for key in input_keys}
    if st.session_state["model_select"] == "XGB Classifier":
        # Send API response to the XGB Classifier API
        xgb_response = requests.post(xgb_endpoint, json=input_features)
        if xgb_response.status_code == 200:
            response_json = xgb_response.json()
            prediction = response_json["prediction"]
            probability = response_json["prediction_probability"]
            st.markdown('---')
            st.success(f"The Sepsis prediction is: {prediction}, with the following prediction probabilities: {probability}")
        else:
            st.error(f"Error: {xgb_response.json().get('error', 'Unknown error')}")
    else:
        # Send API response to the Gradient Boost API
        gradient_boost_response = requests.post(gradient_boost_endpoint, json=input_features)
        if gradient_boost_response.status_code == 200:
            response_json = gradient_boost_response.json()
            prediction = response_json["prediction"]
            probability = response_json["prediction_probability"]
            st.markdown('---')
            st.success(f"The Sepsis prediction is: {prediction}, with the following prediction probabilities: {probability}")
        else:
            st.error(f"Error: {gradient_boost_response.json().get('error', 'Unknown error')}")

if __name__ == "__main__":
    submit_button = display_forms()
    if submit_button:
        make_prediction()
