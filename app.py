import streamlit as st

st.set_page_config(page_title="Smart Unit Converter", page_icon="🔄", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .stApp {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
        }
        .main-title {
            text-align: center;
            font-size: 2.2em;
            font-weight: bold;
            color: #ffcc00;
        }
        .sub-title {
            text-align: center;
            font-size: 1.3em;
            color: #cccccc;
        }
        .stSelectbox, .stNumber_input {
            border: 2px solid #ffcc00 !important;
            border-radius: 8px !important;
        }
        .stSuccess {
            background-color: #32a852;
            padding: 10px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🔄 Smart Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-title'>Convert Weight ⚖️ | Time ⏳ | Length 📏 | Speed 🚀 | Temperature 🌡️</h2>", unsafe_allow_html=True)

conversion_factors = {
    "Weight": {
        "Kilogram (Kg)": 1, "Gram (g)": 1000, "Pound (lb)": 0.4535
, 
        "Tonne": 1000, "Milligram (mg)": 1e-6
    },
    "Time": {
        "Seconds (s)": 1, "Minutes (m)": 60, "Hours (h)": 3600
    },
    "Length": {
        "Meter (m)": 1, "Kilometer (km)": 1000, "Centimeter (cm)": 0.01, 
        "Millimeter (mm)": 0.001, "Mile (mi)": 1609.3444978925634, "Yard (yd)": 0.9144027578387177, 
        "Foot (ft)": 0.3047999902464003, "Inch (in)": 0.025399986284007407
    },
    "Speed": {
        "Meters per second (m/s)": 1, "Kilometers per hour (km/h)": 0.2777777777777778, 
        "Miles per hour (mph)": 0.4470392589877243, "Feet per second (ft/s)": 0.3047999902464003
    },
    "Temperature": {
        "Celsius (°C)": "C", "Fahrenheit (°F)": "F", "Kelvin (K)": "K"
    }
}

unit_type = st.selectbox("📂 Select Category", options=list(conversion_factors.keys()))

unit_from = st.selectbox("🔄 Convert from", options=list(conversion_factors[unit_type].keys()))
unit_to = st.selectbox("🎯 Convert to", options=list(conversion_factors[unit_type].keys()))

quantity = st.number_input("✍️ Enter Quantity:", min_value=0.0, step=1.0)

def convert_temperature(value, from_unit, to_unit):
    """Handles temperature conversions separately."""
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius (°C)":
        return value * 9/5 + 32 if to_unit == "Fahrenheit (°F)" else value + 273.15
    elif from_unit == "Fahrenheit (°F)":
        return (value - 32) * 5/9 if to_unit == "Celsius (°C)" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin (K)":
        return value - 273.15 if to_unit == "Celsius (°C)" else (value - 273.15) * 9/5 + 32

if quantity:
    if unit_type == "Temperature 🌡️":
        converted_value = convert_temperature(quantity, unit_from, unit_to)
        st.success(f"✅ **Converted Value:** `{converted_value} {unit_to}`")
    else:
        if unit_from == unit_to:
            st.info(f"ℹ️ Same unit selected. Answer: `{quantity} {unit_to}`")
        else:
            base_value = quantity * conversion_factors[unit_type][unit_from]  # Convert to base
            converted_value = base_value / conversion_factors[unit_type][unit_to]  # Convert to target unit
            st.success(f"✅ **Converted Value:** `{converted_value} {unit_to}`")

st.markdown("---")
st.markdown("<p style='text-align:center;'>🛠️ <b>Built with ❤️ using Streamlit</b> | 📧 Contact: jakeybooster@gmail.com</p>", unsafe_allow_html=True)
