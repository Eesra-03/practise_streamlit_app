import streamlit as st

st.set_page_config(page_title="Dummy Streamlit Application", layout="wide")

st.title(" Dummy Streamlit App")
st.write("Welcome! This is a sample project structure for Streamlit.")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Hello {name}, this is your dummy Streamlit project!")
