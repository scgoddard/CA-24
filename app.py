import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit Setup and User Interaction
st.title("My First Streamlit App")
st.write("This app demonstrates various Streamlit features.")

# User Input Controls
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age:", 1, 100, 25)
st.write(f"Your age is: {age}")

# Button Interaction
if st.button("Say hello"):
    st.write("Hello there!")

# Data Manipulation and Display
data = {
    "Column 1": [1, 2, 3, 4, 5],
    "Column 2": [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
st.write("Here is a sample DataFrame:")
st.write(df)

# Data Visualization
fig, ax = plt.subplots()
ax.hist(df["Column 2"], bins=5)
st.pyplot(fig)

# Advanced Layouts
col1, col2 = st.columns(2)
with col1:
    st.write("Hello")
with col2:
    st.write("World")

with st.expander("Expand for more information"):
    st.write("Here you could put in some really, really explanatory stuff.")
