import streamlit as st

activity_levels = {
    "Sedentary": {"multiplier": 1.2, "description": "Little or no exercise"},
    "Lightly active": {"multiplier": 1.375, "description": "Light exercise/sports 1-3 days/week"},
    "Moderately active": {"multiplier": 1.55, "description": "Moderate exercise/sports 3-5 days/week"},
    "Very active": {"multiplier": 1.725, "description": "Hard exercise/sports 6-7 days a week"},
    "Extra active": {"multiplier": 1.9, "description": "Very hard exercise/sports & a physical job"}
}


def calculate_bmr(sex, weight, height, age):
    if sex == "Male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

def calculate_tdee(bmr, activity_multiplier):
    return bmr * activity_multiplier

st.title("TDEE Calculator")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Enter your age", min_value=1, max_value=120, step=1, value=25)
    weight = st.number_input("Enter your weight in kilograms", min_value=1, step= 1, value=70)
    height = st.number_input("Enter your height in centimeters", min_value=1, step=1, value=175)

with col2:
    sex = st.selectbox("Select your sex", ["Female", "Male", "Other"], index=1)


    activity_level = st.selectbox(
        "Select your activity level", 
        options=list(activity_levels.keys()),
        index=0, 
        help="Select an activity level based on your regular exercise habits."
    )

    st.caption(f"Explanation: {activity_levels[activity_level]['description']}")


if st.button("Calculate TDEE"):
    # Calculate BMR
    bmr = calculate_bmr(sex, weight, height, age)

    # Get the activity multiplier
    activity_multiplier = activity_levels[activity_level]['multiplier']

    # Calculate TDEE
    tdee = calculate_tdee(bmr, activity_multiplier)
    
    st.write(f"Your estimated Total Daily Energy Expenditure (TDEE) is: {tdee:.2f} calories/day.")
