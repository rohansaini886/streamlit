import streamlit as st

st.title("Find Largest Number")

# Get user input for the three numbers
num1 = st.number_input("Enter First Number:", min_value=float())
num2 = st.number_input("Enter Second Number:", min_value=float())
num3 = st.number_input("Enter Third Number:", min_value=float())

# Find the largest number using built-in max function
largest = max(num1, num2, num3)

# Display the result
if st.button("Find Largest"):
  st.write("The largest number is:", largest)
