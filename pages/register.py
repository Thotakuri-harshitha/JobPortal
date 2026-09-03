import streamlit as st
import json

st.set_page_config(
    page_title="JobPortal - Register",
    page_icon="💼",
    layout="centered"
)

st.title("💼 JobPortal")
st.subheader("Create your account")
st.write("Join JobPortal and start your career journey 🚀")

st.divider()

with st.form("RegisterForm"):

    st.header("📝 Register")

    name = st.text_input(
        "👤 Name",
        placeholder="Enter your name"
    )

    email = st.text_input(
        "📧 Email",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "🔒 Password",
        placeholder="Create a password",
        type="password"
    )

    confirm_password = st.text_input(
        "🔒 Confirm Password",
        placeholder="Re-enter your password",
        type="password"
    )

    role = st.selectbox(
        "💼 Choose Role",
        ["JobSeeker", "Recruiter"]
    )

    register_button = st.form_submit_button(
        "🚀 Create Account",
        use_container_width=True
    )

    if register_button:

        if not name or not email or not password or not confirm_password:
            st.warning("⚠️ Please fill in all the fields.")

        elif password != confirm_password:
            st.error("❌ Passwords do not match.")

        else:

            with open("users.json", "r") as file:
                all_users = json.load(file)

            new_user = {
                "name": name,
                "email": email,
                "password": password,
                "c_password": confirm_password,
                "role": role
            }

            all_users.append(new_user)

            with open("users.json", "w") as file:
                json.dump(all_users, file, indent=4)

            st.success("🎉 Account created successfully!")

            st.switch_page("pages/login.py")