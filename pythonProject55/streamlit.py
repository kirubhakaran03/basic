import streamlit as st
import pickle
import numpy as np

# Streamlit headers
st.header("Rainbow")
st.header("Killer Kirubhakaran", divider="rainbow")

# Slider to input 'n'
n = st.slider("Select an integer (n)", 100, 1000, step=1)

# Dropdown to choose the operation type
choose = st.selectbox("Choose operation type:", ("add", "subtract", "mul", "division"))

# Encoding dictionary for operations
encoded_dict = {"operation": {"add": 1, "subtract": 2, "mul": 3, "division": 4}}


# Function to perform the selected operation
def perform_operation(n, operation):
    if operation == "add":
        result = n + n
    elif operation == "subtract":
        result = n - n  # This results in 0, adjust logic if necessary
    elif operation == "mul":
        result = n * n
    elif operation == "division":
        if n != 0:
            result = n / n
        else:
            result = "Division by zero is not allowed"
    return result


# Function to simulate a model prediction
class MockModel:
    def predict(self, input_array):
        # Simulate a prediction (for example, simply return the input)
        return input_array * 2  # Just an example prediction logic


def model_predict(n):
    try:
        with open("main.pkl", "rb") as file:
            reg_model = pickle.load(file)
            st.write("Data loaded from pickle file.")
            if isinstance(reg_model, int):
                st.write("Loaded data is an integer. Using MockModel for prediction.")
                reg_model = MockModel()
            else:
                st.write("Loaded data is a model.")
    except Exception as e:
        st.write("Failed to load the model:", e)
        reg_model = MockModel()

    # Create an input array for the prediction
    input_array = np.array([[n]])  # Replace the dummy values with actual inputs if needed
    prediction = reg_model.predict(input_array)
    st.write("Prediction made.")
    return prediction


# Button to perform the operation and make the prediction
if st.button("Perform Operation and Predict"):
    # Perform the operation
    operation_result = perform_operation(n, choose)
    st.write(f"Operation Result: {operation_result}")

    # Make the prediction
    prediction = model_predict(operation_result)
    st.write(f"Prediction: {prediction}")
