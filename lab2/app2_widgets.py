import streamlit as st
from datetime import date

# Title
st.title("Widgets Playground")

# 1. Text input
name = st.text_input("Name")

# 2. Number input
age = st.number_input("Age", min_value=1, max_value=100, value=20)

# 3. Slider
marks = st.slider("Marks", min_value=0, max_value=100, value=75)

# 4. Selectbox
city = st.selectbox("City", ["Chennai", "Mumbai", "Delhi"])

# 5. Multiselect
skills = st.multiselect(
    "Skills",
    ["Python", "ML", "SQL", "Streamlit"]
)

# 6. Radio button
gender = st.radio("Gender", ["Male", "Female", "Other"])

# 7. Checkbox
agree = st.checkbox("I agree to terms")

# 8. Date input
dob = st.date_input(
    "Date of Birth",
    value=date(2000, 1, 1)
)

# 9. File uploader
file = st.file_uploader("Upload a file")

# Exercise 1: Color picker
color = st.color_picker("Pick a color", "#00FF00")
st.write("Selected color:", color)

# Exercise 2: Select slider for a range
marks_range = st.select_slider(
    "Select a range of marks",
    options=list(range(0, 101)),
    value=(40, 80)
)
st.write("Range:", marks_range)

# Submit button
if st.button("Submit"):
    st.write("## Submitted Details")

    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Marks:", marks)
    st.write("City:", city)
    st.write("Skills:", skills)
    st.write("Gender:", gender)
    st.write("Agreed:", agree)
    st.write("DOB:", dob)

    # File details
    if file is not None:
        st.write("File uploaded:", file.name)
    else:
        st.info("No file uploaded.")

    # Exercise 3: Print the type of each widget value
    st.write("## Widget Value Types")

    st.write("Name type:", type(name))
    st.write("Age type:", type(age))
    st.write("Marks type:", type(marks))
    st.write("City type:", type(city))
    st.write("Skills type:", type(skills))
    st.write("Gender type:", type(gender))
    st.write("Agree type:", type(agree))
    st.write("DOB type:", type(dob))
    st.write("Color type:", type(color))
    st.write("Marks range type:", type(marks_range))

    if file is not None:
        st.write("File type:", type(file))
