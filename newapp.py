import textwrap

import streamlit as st
import pandas as pd
import joblib

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Heart Risk Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.hero-box {
    background: linear-gradient(135deg, #b71c1c, #e53935);
    padding: 30px 35px;
    border-radius: 18px;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(183, 28, 28, 0.20);
}

.hero-title {
    color: white;
    font-size: 38px;
    font-weight: 700;
    margin: 0;
}

.hero-subtitle {
    color: white;
    font-size: 17px;
    margin-top: 8px;
    opacity: 0.95;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">❤️ Heart Risk Predictor</div>
        <div class="hero-subtitle">
            Machine Learning Based Heart Disease Risk Assessment
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# LOAD MODEL
# ============================================================

try:

    model = joblib.load(
        r"C:\Users\Shubham_kumar\Documents\ML Project 1\Random_heart.pkl"
    )

    scaler = joblib.load(
        r"C:\Users\Shubham_kumar\Documents\ML Project 1\scaler.pkl"
    )

    expected_columns = joblib.load(
        r"C:\Users\Shubham_kumar\Documents\ML Project 1\columns.pkl"
    )

except FileNotFoundError as e:

    st.error("❌ Required model file was not found.")

    st.info(
        "Please make sure Random_heart.pkl, scaler.pkl and "
        "columns.pkl are present in your Downloads folder."
    )

    st.code(str(e))

    st.stop()

except Exception as e:

    st.error("❌ Error while loading the ML model.")
    st.code(str(e))

    st.stop()


# ============================================================
# HEADER
# ============================================================




# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("❤️ About")

    st.write(
        """
        This application uses a trained Machine Learning model
        to estimate the risk of heart disease based on the
        information provided.
        """
    )

    st.divider()

    st.subheader("📌 Model")

    st.write("Random Forest")

    st.subheader("📊 Input Parameters")

    st.write("10+ clinical parameters")

    st.divider()

    st.warning(
        """
        **Disclaimer**

        This application is for educational and demonstration
        purposes only. It is not a medical diagnosis.
        """
    )


# ============================================================
# PATIENT INFORMATION
# ============================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("👤 Patient Information")

col1, col2, col3 = st.columns(3)

with col1:

    age = st.slider(
        "🎂 Age",
        min_value=18,
        max_value=100,
        value=40,
        help="Select patient's age."
    )

with col2:

    sex = st.selectbox(
        "⚥ Sex",
        ["M", "F"],
        help="Select biological sex."
    )

with col3:

    resting_bp = st.number_input(
        "🩸 Resting Blood Pressure",
        min_value=80,
        max_value=200,
        value=120,
        step=1,
        help="Resting blood pressure in mm Hg."
    )

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# HEART PARAMETERS
# ============================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("🫀 Heart & Clinical Parameters")

col1, col2 = st.columns(2)

with col1:

    chest_pain = st.selectbox(
        "💓 Chest Pain Type",
        ["ATA", "NAP", "TA", "ASY"],
        help="""
        ATA = Atypical Angina
        NAP = Non-Anginal Pain
        TA = Typical Angina
        ASY = Asymptomatic
        """
    )

    cholesterol = st.number_input(
        "🧪 Cholesterol (mg/dL)",
        min_value=100,
        max_value=600,
        value=200,
        step=1
    )

    fasting_bs = st.selectbox(
        "🍬 Fasting Blood Sugar > 120 mg/dL",
        [0, 1],
        format_func=lambda x:
            "Yes" if x == 1 else "No"
    )

with col2:

    resting_ecg = st.selectbox(
        "📈 Resting ECG",
        ["Normal", "ST", "LVH"],
        help="""
        Normal = Normal ECG
        ST = ST-T wave abnormality
        LVH = Left ventricular hypertrophy
        """
    )

    max_hr = st.slider(
        "❤️ Maximum Heart Rate",
        min_value=60,
        max_value=220,
        value=150
    )

    exercise_angina = st.selectbox(
        "🏃 Exercise-Induced Angina",
        ["Y", "N"],
        format_func=lambda x:
            "Yes" if x == "Y" else "No"
    )

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# ECG PARAMETERS
# ============================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("📊 ECG & Exercise Parameters")

col1, col2 = st.columns(2)

with col1:

    oldpeak = st.slider(
        "📉 Oldpeak (ST Depression)",
        min_value=0.0,
        max_value=6.0,
        value=1.0,
        step=0.1
    )

with col2:

    st_slope = st.selectbox(
        "📈 ST Slope",
        ["Up", "Flat", "Down"]
    )

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# INPUT SUMMARY
# ============================================================

with st.expander("🔍 Review Patient Information"):

    summary_data = {
        "Parameter": [
            "Age",
            "Sex",
            "Chest Pain",
            "Resting BP",
            "Cholesterol",
            "Fasting Blood Sugar",
            "Resting ECG",
            "Maximum Heart Rate",
            "Exercise Angina",
            "Oldpeak",
            "ST Slope"
        ],

        "Value": [
            f"{age} years",
            sex,
            chest_pain,
            f"{resting_bp} mm Hg",
            f"{cholesterol} mg/dL",
            "Yes" if fasting_bs == 1 else "No",
            resting_ecg,
            f"{max_hr} bpm",
            "Yes" if exercise_angina == "Y" else "No",
            oldpeak,
            st_slope
        ]
    }

    summary_df = pd.DataFrame(summary_data)

    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.markdown("### 🎯 Ready to Check Risk?")

predict_col, reset_col = st.columns([3, 1])

with predict_col:

    predict_button = st.button(
        "🔍 ANALYZE HEART RISK",
        type="primary",
        use_container_width=True
    )

with reset_col:

    reset_button = st.button(
        "🔄 Reset",
        use_container_width=True
    )

if reset_button:

    st.rerun()


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    try:

        # ----------------------------------------------------
        # Create raw input dictionary
        # ----------------------------------------------------

        raw_input = {

            "Age": age,

            "RestingBP": resting_bp,

            "Cholesterol": cholesterol,

            "FastingBS": fasting_bs,

            "MaxHR": max_hr,

            "Oldpeak": oldpeak,

            "Sex_" + sex: 1,

            "ChestPainType_" + chest_pain: 1,

            "RestingECG_" + resting_ecg: 1,

            "ExerciseAngina_" + exercise_angina: 1,

            "ST_Slope_" + st_slope: 1
        }


        # ----------------------------------------------------
        # Create dataframe
        # ----------------------------------------------------

        input_df = pd.DataFrame([raw_input])


        # ----------------------------------------------------
        # Add missing columns
        # ----------------------------------------------------

        for col in expected_columns:

            if col not in input_df.columns:

                input_df[col] = 0


        # ----------------------------------------------------
        # Remove unexpected columns
        # ----------------------------------------------------

        input_df = input_df.reindex(
            columns=expected_columns,
            fill_value=0
        )


        # ----------------------------------------------------
        # Scale input
        # ----------------------------------------------------

        scaled_input = scaler.transform(input_df)


        # ----------------------------------------------------
        # Prediction
        # ----------------------------------------------------

        prediction = model.predict(scaled_input)[0]


        # ----------------------------------------------------
        # Probability
        # ----------------------------------------------------

        probability = None

        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(scaled_input)[0]

            probability = probabilities[1] * 100


        # ====================================================
        # RESULT
        # ====================================================

        st.divider()

        st.subheader("📋 Prediction Result")


        if prediction == 1:

            st.markdown(
                f"""
                <div class="risk-high">

                    <h2>⚠️ Higher Risk Detected</h2>

                    <p>
                    The Machine Learning model has classified
                    this input as <b>higher risk</b>.
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            if probability is not None:

                st.metric(
                    "Estimated Model Probability",
                    f"{probability:.2f}%"
                )

            st.warning(
                "This result is not a medical diagnosis. "
                "Please consult a qualified healthcare professional "
                "for proper evaluation."
            )


        else:

            st.markdown(
                textwrap.dedent(f"""
                <div class="risk-low">
                    <h2>✅ Lower Risk Detected</h2>
                    <p>
                        The Machine Learning model has classified
                        this input as <b>lower risk</b>.
                    </p>
                </div>
                """),
                unsafe_allow_html=True
            )

            if probability is not None:

                st.metric(
                    "Estimated Model Probability",
                    f"{probability:.2f}%"
                )

            st.success(
                "The model predicts a lower risk based on "
                "the provided parameters."
            )


        # ====================================================
        # MODEL DETAILS
        # ====================================================

        with st.expander("🤖 Model Prediction Details"):

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Prediction",
                    "High Risk" if prediction == 1
                    else "Low Risk"
                )

            with col2:

                if probability is not None:

                    st.metric(
                        "Risk Probability",
                        f"{probability:.2f}%"
                    )

                else:

                    st.metric(
                        "Probability",
                        "Not Available"
                    )

            with col3:

                st.metric(
                    "Model",
                    "Random Forest"
                )


        # ====================================================
        # INPUT DATA
        # ====================================================

        with st.expander("📄 Model Input Data"):

            st.dataframe(
                input_df,
                use_container_width=True
            )


    except Exception as e:

        st.error(
            "❌ An error occurred while making the prediction."
        )

        st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    ❤️ Heart Risk Predictor |
    Machine Learning Demonstration |
    Developed by Shubham Kumar

    ⚠️ For educational purposes only. Not a substitute for
    professional medical advice.
     
</div> 
""", unsafe_allow_html=True)