import streamlit as st
import json 

st.title("💼Job Portal")

if st.button("⏩login"):
    st.switch_page("pages/login.py")

if st.button("⏩register"):
    st.switch_page("pages/register.py")