import streamlit as st

if "loggedin_user" not in st.session_state:
    st.warning("⚠️Please login first")
    st.switch_page("pages/login.py")

else:

    if st.session_state["loggedin_user"]["role"] == "Recruiter":

        st.title("💼Recruiter Dashboard")

        st.write("💼Welcome Recruiter!")

    else:

        st.warning(
            " ⚠️You are not allowed to access this page"
        )