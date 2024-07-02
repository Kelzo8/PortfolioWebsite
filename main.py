import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)


with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("James Kelly")
    content = """
    Hi I am a software engineering student
    """
    st.info(content)

content2 = """
Below you can see some of my projects which I have worked on both by myself and in a team"""
st.write(content2)