import streamlit as st

# Set page title
st.set_page_config(page_title="Temperature Converter", page_icon=":thermometer:", layout="wide")

# App Title
st.title("Temperature Converter")
st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin.")

# User input for temperature value
temp_value = st.number_input("Enter the temperature value:")

# User input for temperature unit selection
temp_unit = st.selectbox("Select the unit of temperature", ("Celsius", "Fahrenheit", "Kelvin"))

# Function to convert temperature
def convert_temperature(value, unit):
    if unit == "Celsius":
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return fahrenheit, kelvin
    elif unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
        kelvin = (value - 32) * 5/9 + 273.15
        return celsius, kelvin
    elif unit == "Kelvin":
        celsius = value - 273.15
        fahrenheit = (value - 273.15) * 9/5 + 32
        return celsius, fahrenheit

# Convert temperature when button is pressed
if st.button("Convert Temperature"):
    if temp_value:
        converted_values = convert_temperature(temp_value, temp_unit)
        if temp_unit == "Celsius":
            st.write(f"{temp_value} °C is equal to {converted_values[0]:.2f} °F and {converted_values[1]:.2f} K.")
        elif temp_unit == "Fahrenheit":
            st.write(f"{temp_value} °F is equal to {converted_values[0]:.2f} °C and {converted_values[1]:.2f} K.")
        elif temp_unit == "Kelvin":
            st.write(f"{temp_value} K is equal to {converted_values[0]:.2f} °C and {converted_values[1]:.2f} °F.")
    else:
        st.write("Please enter a valid temperature value.")

