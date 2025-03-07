# # Project 8 : BMI CALCULATOR IN PYTHON STREAMLIT APP

#
import streamlit as st  # type: ignore

# Configure page
st.set_page_config(
    page_title="Pro Neon BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

# Custom CSS for enhanced neon styling
st.markdown("""
    <style>
        body { background-color: #0d0d0d; }
        .stApp { background: linear-gradient(to right, #8A2BE2, #FF007F, #FF1493); color: white; }
        .title { text-align: center; font-size: 36px; font-weight: bold; color: #4B0082; text-shadow: 2px 2px 10px #FF007F; }
        .bmi-result { font-size: 24px; font-weight: bold; padding: 15px; border-radius: 12px; text-align: center; color: #4B0082; text-shadow: 2px 2px 10px white; }
        .radio-label { color: #FF007F; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# App header
st.markdown("<p class='title'>🚀 Pro Neon BMI Calculator</p>", unsafe_allow_html=True)
st.markdown("---")

# Weight units selection
unit = st.radio("Select Measurement System:",
               ["Metric (kg & meters)", "Imperial (lbs & inches)"],
               horizontal=True)

# Input fields
with st.form("bmi_form"):
    if "Metric" in unit:
        weight = st.number_input("Enter Weight (kg)", min_value=1.0, max_value=300.0, value=70.0)
        height = st.number_input("Enter Height (meters)", min_value=0.5, max_value=3.0, value=1.75)
    else:
        weight = st.number_input("Enter Weight (lbs)", min_value=1.0, max_value=660.0, value=154.0)
        col1, col2 = st.columns(2)
        with col1:
            feet = st.number_input("Feet", min_value=1, max_value=8, value=5)
        with col2:
            inches = st.number_input("Inches", min_value=0, max_value=11, value=9)
        height = (feet * 12 + inches) * 0.0254  # Convert to meters

    submitted = st.form_submit_button("💡 Calculate BMI")

# BMI Calculation
if submitted:
    try:
        if "Metric" in unit:
            bmi = weight / (height ** 2)
        else:
            bmi = (weight * 703) / ((height / 0.0254) ** 2)

        if bmi < 18.5:
            bmi_category = "Underweight 🏋️"
            color = "#8A2BE2"
        elif 18.5 <= bmi < 25:
            bmi_category = "Normal Weight ✅"
            color = "#FF007F"
        elif 25 <= bmi < 30:
            bmi_category = "Overweight ⚠️"
            color = "#FF1493"
        else:
            bmi_category = "Obese ❌"
            color = "#DC143C"

        # Display results
        st.markdown("---")
        st.markdown(f"""
            <div class='bmi-result' style='background-color:{color};'>
                Your BMI: {bmi:.1f} <br> {bmi_category}
            </div>
        """, unsafe_allow_html=True)
    except ZeroDivisionError:
        st.error("Please enter a valid height greater than zero.")

# BMI Classification Chart
with st.expander("📊 BMI Classification Chart"):
    st.markdown("""
    | BMI Range       | Category        |
    |----------------|-----------------|
    | Below 18.5      | Underweight     |
    | 18.5 - 24.9     | Normal Weight   |
    | 25.0 - 29.9     | Overweight      |
    | 30.0 and above  | Obese           |
    """)

# Health Tips
st.markdown("---")
st.subheader("💡 Health Tips")
st.write("""
- 🥗 Maintain a balanced diet
- 🏃 Exercise regularly (150 mins/week)
- 😴 Get enough sleep (7-9 hours)
- 💧 Stay hydrated (2-3 liters/day)
- ⚖️ Monitor your weight regularly
""")

# Disclaimer
st.markdown("---")
st.caption("⚠️ Note: BMI is a simple screening tool and does not account for muscle mass or body composition.")
