# voting_system.py

import streamlit as st
import pandas as pd

# Title
st.title("Simple Voting System")

# Voter authentication (basic example)
voters = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
}

# Candidates
candidates = ["Alice", "Bob", "Charlie"]

# Store votes
if "votes" not in st.session_state:
    st.session_state["votes"] = {candidate: 0 for candidate in candidates}

# Authenticate Voter
username = st.text_input("Enter your username:")
password = st.text_input("Enter your password:", type="password")

if st.button("Login"):
    if username in voters and voters[username] == password:
        st.success("Login successful!")
        st.session_state["voter_authenticated"] = True
    else:
        st.error("Invalid username or password.")

# Voting Section
if st.session_state.get("voter_authenticated", False):
    st.header("Vote for your candidate")
    vote = st.radio("Select a candidate:", candidates)

    if st.button("Submit Vote"):
        st.session_state["votes"][vote] += 1
        st.success(f"Vote submitted for {vote}!")
        st.session_state["voter_authenticated"] = False  # Prevent re-voting

# Display results (admin view)
if st.checkbox("Show Results (Admin Only)"):
    results_df = pd.DataFrame.from_dict(st.session_state["votes"], orient="index", columns=["Votes"])
    st.write(results_df)
