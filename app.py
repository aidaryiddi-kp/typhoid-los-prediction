import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="BMC | Typhoid LOS Predictor",
    page_icon="🏥",
    layout="centered"
)

st.markdown("""
    <style>
    .main-title {
        color: #0B5394 !important;
        font-size: 48px !important;
        font-weight: 800 !important;
        margin-bottom: 0px !important;
        line-height: 1.1 !important;
    }
    .sub-title {
        color: #555555 !important;
        font-size: 10px !important;
        margin-top: 0px !important;
    }
    .result-box {
        background-color: #E8F0FE;
        padding: 20px;
        border-radius: 18px;
        border-left: 6px solid #0B5394;
    }
    </style>
""", unsafe_allow_html=True)

model = joblib.load("random_forest_los_model.pkl")
model_columns = joblib.load("model_columns.pkl")


col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image("BMC_LOGO.jpeg", width=100)
with col_title:
    st.markdown('<p class="main-title">Bugando Medical Centre</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Department of ICT — Clinical Decision Support System</p>', unsafe_allow_html=True)

st.divider()
st.subheader("🩺 Typhoid Patient — Length of Stay Predictor")
st.caption("Estimates expected hospital stay to support ward and bed-capacity planning.")

st.markdown("#### 👤 Patient Demographics")
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    gender = st.selectbox("Gender", ["Male", "Female"])
with col2:
    admission_type = st.selectbox("Admission Type", ["Emergency", "Referral", "Elective"])
    insurance = st.selectbox("Insurance Type", ["Cash", "NHIF", "Private", "Exempted"])

st.markdown("#### 🧪 Clinical Information")
col3, col4 = st.columns(2)
with col3:
    ward = st.selectbox("Ward Department", ["Male Medical", "Female Medical", "Pediatrics", "ICU"])
    comorbidities = st.number_input("Comorbidities Count", min_value=0, max_value=10, value=0)
    temperature = st.number_input("Temperature (°C)", min_value=35.0, max_value=42.0, value=37.5)
with col4:
    bowel_perforation = st.selectbox("Bowel Perforation", ["No", "Yes"])
    widal = st.selectbox("Widal Test Result", ["Negative", "Positive (1:160)", "Positive (1:320)"])
    stool = st.selectbox("Stool Culture", ["Negative", "Positive", "Pending"])

st.write("")
predict_btn = st.button("🔍 Predict Length of Stay", use_container_width=True, type="primary")


if predict_btn:

    input_dict = {
        "Age": age,
        "Comorbidities_Count": comorbidities,
        "Bowel_Perforation": 1 if bowel_perforation == "Yes" else 0,
        "Temperature_C": temperature,
        f"Gender_{gender}": 1,
        f"Admission_Type_{admission_type}": 1,
        f"Ward_Department_{ward}": 1,
        f"Widal_Test_{widal}": 1,
        f"Stool_Culture_{stool}": 1,
        f"Insurance_Type_{insurance}": 1,
    }

    input_df = pd.DataFrame([input_dict])
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_df)[0]

    st.divider()
    st.markdown(
        f"""
        <div class="result-box">
            <h4>📋 Estimated Length of Stay</h4>
            <h2 style="color:#0B5394;">{prediction:.1f} days</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    if prediction > 8:
        st.warning("⚠️ Extended stay predicted — consider prioritizing bed and resource allocation.")
    else:
        st.success("✅ Expected within normal typhoid recovery range.")

st.divider()
st.caption("Bugando Medical Centre | ICT Department | 🙏 Thank you for using our service — Enjoy!")
