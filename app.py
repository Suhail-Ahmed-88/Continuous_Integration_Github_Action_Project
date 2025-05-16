import streamlit as st

#Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square,cube, and fifth power")

#Get user input
n = st.number_input("Enter a integer", value=1, step=1)

# Calculate results
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

# Display_results
st.write(f"The Square of {n} is: {square}")
st.write(f"The Cube of {n} is: {cube}")
st.write(f"The Fifth Power of {n} is: {fifth_power}")