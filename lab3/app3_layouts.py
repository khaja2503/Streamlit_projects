import streamlit as st
import pandas as pd
import numpy as np

# Page title
st.title("Layouts Demo")

st.write("Learn how to organize a Streamlit application.")

st.sidebar.header("Settings")

theme = st.sidebar.selectbox(
    "Theme",
    ["Light", "Dark"]
)

font_size = st.sidebar.slider(
    "Font Size",
    min_value=10,
    max_value=30,
    value=15
)

st.sidebar.write("Selected theme:", theme)
st.sidebar.write("Selected font size:", font_size)

# Apply selected font size to displayed content
st.markdown(
    f"""
    <style>
    .stApp {{
        font-size: {font_size}px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Main Area")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", "25 Lakh")

with col2:
    st.metric("Customers", "1,200")

st.header("Exercise 1: Three Columns")

c1, c2, c3 = st.columns([1, 2, 1])

with c1:
    st.write("Left (narrow)")

with c2:
    st.write("Center (wide)")

with c3:
    st.write("Right (narrow)")

np.random.seed(42)

df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.divider()

st.header("Tabs Demo")

tab1, tab2, tab3 = st.tabs(
    ["Overview", "Analysis", "About"]
)

with tab1:
    st.subheader("Line Chart")
    st.write("Overview of sample data.")
    st.line_chart(df)

with tab2:
    st.subheader("Bar Chart")
    st.write("Compare values of A, B and C.")
    st.bar_chart(df)

with tab3:
    st.subheader("About This App")
    st.write("This application demonstrates Streamlit layouts.")
    st.write("It uses columns, sidebar, tabs and containers.")

st.divider()
st.header("Exercise 2: Expander")

with st.expander("Details"):
    st.write("This content is hidden until expanded.")
    st.write("You can put anything here.")
    st.write("The charts use randomly generated sample data.")

st.divider()

with st.container():
    st.subheader("Grouped Section")
    st.write("All these elements are inside one container.")
    st.write("Container helps organize related content.")

st.success("Layouts Demo completed!")
