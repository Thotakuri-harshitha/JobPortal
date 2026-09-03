import streamlit as st
import json

st.set_page_config(
    page_title="JobPortal - Login",
    page_icon="💼",
    layout="centered"
)

st.title("💼 JobPortal")
st.subheader("Welcome back 👋")
st.write("Login to continue your journey 🚀")

st.divider()

with st.form("LoginForm"):

    st.header("🔐 Login")

    email = st.text_input(
        "📧 Email",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "🔒 Password",
        placeholder="Enter your password",
        type="password"
    )

    role = st.selectbox(
        "💼 Choose Role",
        ["JobSeeker", "Recruiter"]
    )

    login_button = st.form_submit_button(
        "🔑 Login",
        use_container_width=True
    )

    if login_button:

        if not email or not password:
            st.warning("⚠️ Please enter your email and password.")

        else:

            with open("users.json", "r") as file:
                all_users = json.load(file)

            user_found = False

            for user in all_users:

                if (
                    user["email"] == email
                    and user["password"] == password
                    and user["role"] == role
                ):

                    user_found = True

                    st.session_state["loggedin_user"] = {
                        "email": email,
                        "role": role
                    }

                    st.success("🎉 Login successful!")

                    if role == "JobSeeker":
                        st.switch_page(
                            "pages/JobSeekerDashboard.py"
                        )

                    elif role == "Recruiter":
                        st.switch_page(
                            "pages/RecruiterDashboard.py"
                        )

                    break

            if not user_found:
                st.error("❌ Invalid email, password or role.")