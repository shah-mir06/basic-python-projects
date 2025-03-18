
import streamlit as st

st.title(" BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) easily.")

weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.1f")
height = st.number_input("Enter your height (cm)", min_value=50.0, format="%.1f")

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        height_m = height / 100  
        bmi = weight / (height_m ** 2)  
        
        if bmi < 18.5:
            category = "Underweight"
            color = "blue"

        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight"
            color = "green"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"
        
        st.subheader(f"Your BMI: {bmi:.2f}")
        st.markdown(f"**Category:** <span style='color:{color}; font-size:20px;'>{category}</span>", unsafe_allow_html=True)
        
        st.progress(min(int(bmi * 2.5), 100))
    else:
        st.warning("Please enter valid weight and height values.")