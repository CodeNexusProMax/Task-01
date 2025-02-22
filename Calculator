import streamlit as st
from datetime import datetime

# Set page title
st.set_page_config(page_title="Age Calculator", page_icon=":calendar:", layout="wide")

# App Title
st.title("Age Calculator")
st.write("Enter your date of birth to calculate your age.")

# Get today's date
today = datetime.today().date()

# User input for date of birth with no limit on past dates (from 1900 to today's date)
dob = st.date_input("Select your date of birth:", max_value=today, min_value=datetime(1900, 1, 1))

# Function to calculate age
def calculate_age(dob):
    today = datetime.today().date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

# Calculate age when button is pressed
if st.button("Calculate Age"):
    if dob:
        age = calculate_age(dob)
        st.write(f"You are {age} years old.")
    else:
        st.write("Please select your date of birth.")
