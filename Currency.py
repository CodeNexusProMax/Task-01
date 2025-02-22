import streamlit as st

# Set page title
st.set_page_config(page_title="Currency Converter", page_icon=":money_with_wings:", layout="wide")

# App Title
st.title("Currency Converter")
st.write("Enter the amount in PKR and select the currency to convert.")

# User input for amount in PKR
pkr_amount = st.number_input("Enter amount in PKR:", min_value=0.0, step=1.0)

# Dropdown menu for currency conversion
currency = st.selectbox("Select the currency to convert to", ("USD", "GBP (UK)", "INR (India)", "CNY (China)","Ruble (Russia)"))

# Conversion rates (fixed rates, these can be updated if needed)
conversion_rates = {
    "USD": 0.0036,   # 1 PKR = 0.0061 USD
    "GBP (UK)": 0.0028, # 1 PKR = 0.0048 GBP
    "INR (India)": 0.31,  # 1 PKR = 0.51 INR
    "CNY (China)": 0.026, # 1 PKR = 0.041 CNY
    "Ruble (Russia)": 0.32
}

# Function to convert PKR to selected currency
def convert_currency(pkr, currency):
    if currency in conversion_rates:
        return pkr * conversion_rates[currency]
    else:
        return "Invalid currency"

# Conversion and display when button is pressed
if st.button("Convert Currency"):
    if pkr_amount > 0:
        converted_amount = convert_currency(pkr_amount, currency)
        st.write(f"{pkr_amount} PKR is equal to {converted_amount:.2f} {currency}.")
    else:
        st.write("Please enter a valid amount in PKR.")
