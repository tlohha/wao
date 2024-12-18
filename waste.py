import streamlit as st
import pandas as pd

# Initialize data storage
if "users" not in st.session_state:
    st.session_state["users"] = []
if "requests" not in st.session_state:
    st.session_state["requests"] = []

# App Title
st.title("WASTE MANAGEMENT SYSTEM")

# Tabs for User and Admin Views
tab1, tab2 = st.tabs(["User View", "Admin View"])

# User View
with tab1:
    st.header("User Portal")

    # User Registration
    st.subheader("Register")
    user_name = st.text_input("Enter your name:")
    user_location = st.text_input("Enter your location:")
    if st.button("Register"):
        if user_name and user_location:
            st.session_state["users"].append({"name": user_name, "location": user_location})
            st.success("Registration successful!")
        else:
            st.error("Please fill in all fields.")

    # Submit Waste Collection Request
    st.subheader("Request Waste Collection")
    if len(st.session_state["users"]) > 0:
        user = st.selectbox("Select your name:", [user["name"] for user in st.session_state["users"]])
        waste_type = st.selectbox("Type of Waste:", ["Plastic", "Organic", "BORONGOTO", "MAKARATASI", "VYUMA CHAKAVU"])
        if st.button("Submit Request"):
            st.session_state["requests"].append({"user": user, "waste_type": waste_type, "status": "Pending"})
            st.success("Request submitted successfully!")
    else:
        st.warning("No registered users found. Please register first.")

# Admin View
with tab2:
    st.header("Admin Portal")

    # Display Requests
    st.subheader("Waste Collection Requests")
    if len(st.session_state["requests"]) > 0:
        requests_df = pd.DataFrame(st.session_state["requests"])
        st.dataframe(requests_df)

        # Update Status
        request_index = st.number_input("Enter the request number to update:", min_value=0, max_value=len(st.session_state["requests"]) - 1, step=1)
        new_status = st.selectbox("Update status to:", ["Pending", "In Progress", "Completed"])
        if st.button("Update Status"):
            st.session_state["requests"][request_index]["status"] = new_status
            st.success("Status updated successfully!")
    else:
        st.info("No requests found.")

# Footer
st.write("---")
st.write("Developed by DANIEL")
