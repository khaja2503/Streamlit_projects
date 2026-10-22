import streamlit as st

# Page configuration - Exercise 1: Wide layout
st.set_page_config(
    page_title="Hello App",
    page_icon="H",
    layout="wide"
)

# Greeting function
def greet(name):
    return f"Hello, {name}!"

# Headings
st.title("Hello Streamlit")
st.header("My First App")
st.subheader("Learning Basics")

# Text elements
st.write("Streamlit converts Python scripts into web apps.")
st.markdown("**Bold**, *Italic*, and `Code` work here.")

# Messages
st.success("App loaded successfully!")
st.info("This is an info message.")
st.warning("This is a warning.")
st.error("This is an error.")

# User inputs
name = st.text_input("Enter your name")

age = st.number_input("Enter your age", min_value=1, max_value=100)

# Display name and personalized greeting
if name.strip():
    st.write("Your name is:", name)
    st.success(greet(name))

st.write("Your age is:", age)

# Sample table
st.write("### Sample Data")

st.table({
    "Name": ["A", "B"],
    "Marks": [85, 90]
})

# Exercise 2: Display Python code
st.write("### Exercise 2: Code Example")

st.code("""
def greet(name):
    return f"Hello, {name}!"
""", language="python")

# Exercise 3: Add a divider
st.divider()
