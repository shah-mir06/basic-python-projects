import streamlit as st

def check_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    return score

st.title("Welcome to Password Strength Meter.")
st.markdown("---")
password = st.text_input("Enter your password:", type="password")

if st.button("Check Password"):
    if password:
        score = check_password(password)
        if score == 0:
            st.write("Very Weak Password")
        elif score == 1:
            st.write("Weak Password")
        elif score == 2:
            st.write("Moderate Password")
        else:
            st.write("Strong Password")
    else:
        ("Please Enter your Password")

st.markdown("---")
st.write("\n**Developed by Shah Mir**")



# **Password Strength Meter - Complete Guide**

# ## **Project Overview**
# This project is a **Password Strength Meter** built using **Python** and **Streamlit**. It evaluates the strength of a password based on its length, presence of uppercase letters, digits, and special characters. It provides feedback on whether the password is weak or strong.

# ## **How It Works**
# The program follows a **simple scoring system** to determine password strength:
# - **Score 0** → Very Weak Password
# - **Score 1** → Weak Password
# - **Score 2** → Moderate Password
# - **Score 3 or More** → Strong Password

# The password is analyzed based on four main criteria:
# 1. Length (at least 8 characters)
# 2. Presence of an uppercase letter
# 3. Presence of a digit
# 4. Presence of a special character (!@#$%^&*)

# Each criterion met increases the score by 1.

# ---

# ## **Code Breakdown**

# ### **1. Importing Streamlit**
# ```python
# import streamlit as st
# ```
# - Streamlit is used to create the user interface.
# - `st` is the shorthand for Streamlit functions.

# ---

# ### **2. Function to Check Password Strength**
# ```python
# def check_password(password):
#     score = 0
#     if len(password) >= 8:
#         score += 1
#     if any(c.isupper() for c in password):
#         score += 1
#     if any(c.isdigit() for c in password):
#         score += 1
#     if any(c in "!@#$%^&*" for c in password):
#         score += 1
#     return score
# ```

# #### **Logic Explained:**
# - `score = 0` → The score starts at 0.
# - `if len(password) >= 8:` → If the password is **at least 8 characters long**, `score` increases by 1.
# - `if any(c.isupper() for c in password):` → If the password contains an **uppercase letter**, `score` increases by 1.
# - `if any(c.isdigit() for c in password):` → If the password has **a number (0-9)**, `score` increases by 1.
# - `if any(c in "!@#$%^&*" for c in password):` → If the password contains **a special character**, `score` increases by 1.
# - `return score` → Returns the final strength score.

# ---

# ### **3. Streamlit UI - Displaying the Password Meter**
# ```python
# st.title("Password Strength Meter")
# st.markdown("---")
# password = st.text_input("Enter your password:", type="password")

# if st.button("Check Password"):
#     if password:
#         score = check_password(password)
#         if score == 0:
#             st.write("Very Weak Password")
#         elif score == 1:
#             st.write("Weak Password")
#         elif score == 2:
#             st.write("Moderate Password")
#         else:
#             st.write("Strong Password")
#     else:
        # st.write("Please enter a password.")


# #### **Logic Explained:**
# - `st.markdown("---")` → Adds a horizontal line for better UI separation.
# - `st.text_input()` → Creates a password input field where users can enter their password (hidden as `****`).
# - `st.button("Check Password")` → Adds a **button** that the user must click to check the password.
# - If the button is clicked:
#   - Calls `check_password()` to **calculate the password score**.
#   - Displays:
#     - **0 → Very Weak Password**
#     - **1 → Weak Password**
#     - **2 → Moderate Password**
#     - **3 or more → Strong Password**
#   - If no password is entered, it prompts: "Please enter a password."

# ---

# ### **4. Footer - Displaying the Developer's Name**
# ```python
# st.markdown("---")
# st.write("\n**Developed by Shah Mir**")
# ```
# - Adds another horizontal line for better UI.
# - Displays "Developed by Shah Mir" at the bottom.

# ---

# ## **How to Run the Project**

# ### **1. Install Streamlit (if not installed)**
# ```sh
# pip install streamlit
# ```

# ### **2. Run the App**
# ```sh
# streamlit run filename.py
# ```
# - Replace `filename.py` with your actual Python file name.

# ---

# ## **Improvements & Additional Features**
# ✅ **Password Generator:** Suggests a strong password.
# ✅ **Blacklist Common Passwords:** Rejects weak passwords like `password123`.
# ✅ **Better UI with Colors:** Highlight weak/strong passwords using colors.
# ✅ **More Password Rules:** Require more complex password structures.

# ---

# This guide provides a **step-by-step explanation** of how the password strength meter works, now with a **button to check passwords**. Let me know if you have any questions! 🚀