import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#load model
model=pickle.load(open('model-kidney-desease.pkl','rb'))
scaller=pickle.load(open('scaller-kidney-desease.pkl','rb'))


# define function Prediction on new data usinf function
def predict_chronic_disease(age, bp, sg, al, hemo, sc, htn, dm, cad, appet, pc):
    # Create a DataFrame with input variables, following the correct order
    df_dict = {
        'age': [age],
        'bp': [bp],
        'sg': [sg],
        'al': [al],
        'hemo': [hemo],
        'sc': [sc],
        'htn': [htn],
        'dm': [dm],
        'cad': [cad],
        'appet': [appet],
        'pc': [pc]
    }
    df = pd.DataFrame(df_dict)

    # Encode the categorical columns
    le = LabelEncoder()
    df['htn'] = le.fit_transform(df['htn'])
    df['dm'] = le.fit_transform(df['dm'])
    df['cad'] = le.fit_transform(df['cad'])
    df['appet'] = le.fit_transform(df['appet'])
    df['pc'] = le.fit_transform(df['pc'])

    # Scale the numeric columns using the previously fitted scaler
    numeric_cols = ['age', 'bp', 'sg', 'al', 'hemo', 'sc']
    df[numeric_cols] = scaller.transform(df[numeric_cols])

    # Make the prediction
    prediction = model.predict(df)

    # Return the predicted class
    return prediction[0]


# Streamlit UI
# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#f5f7fb;
}

.block-container{
    padding-top:2.5rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

.big-title{
    font-size:30px;
    font-weight:bold;
    color:#1565C0;
    text-align:center;
}

.sub-title{
    text-align:center;
    color:#666;
    font-size:18px;
    margin-bottom:25px;
}

.stButton>button{
    width:100%;
    background:#1565C0;
    color:white;
    font-size:22px;
    font-weight:bold;
    border-radius:10px;
    height:60px;
}

.stButton>button:hover{
    background:#0d47a1;
    color:white;
}

div[data-testid="stNumberInput"],
div[data-testid="stSelectbox"]{
    background:white;
    padding:5px;
    border-radius:10px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# Header
# ---------------------------------------

st.markdown("<div class='big-title'>Chronic Kidney Disease Prediction</div>",
            unsafe_allow_html=True)

st.markdown(
"<div class='sub-title'>Developed by <b>Muhammad Akhtar</b> | 📱03215261156</div>",
unsafe_allow_html=True)

#st.divider()
st.subheader("👤 Patient Details")
# ---------------------------------------
# Three Columns
# ---------------------------------------

col1, col2, col3 = st.columns(3)

with col1:



    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=48
    )

    bp = st.number_input(
        "Blood Pressure",
        min_value=40,
        max_value=200,
        value=80
    )

    sg = st.number_input(
        "Specific Gravity",
        min_value=1.005,
        max_value=1.050,
        value=1.020,
        format="%.3f"
    )

    al = st.number_input(
        "Albumin",
        min_value=0.0,
        max_value=5.0,
        value=1.0
    )


with col2:



    hemo = st.number_input(
        "Hemoglobin",
        min_value=5.0,
        max_value=20.0,
        value=15.4
    )

    sc = st.number_input(
        "Serum Creatinine",
        min_value=0.5,
        max_value=10.0,
        value=1.2
    )

    htn = st.selectbox(
        "Hypertension",
        ["yes","no"]
    )

    dm = st.selectbox(
        "Diabetes",
        ["yes","no"]
    )


with col3:



    cad = st.selectbox(
        "Coronary Artery Disease",
        ["yes","no"]
    )

    appet = st.selectbox(
        "Appetite",
        ["good","poor"]
    )

    pc = st.selectbox(
        "Protein in Urine",
        ["normal","abnormal"]
    )

    st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------
# Predict Button
# ---------------------------------------

if st.button("🔍 Predict Kidney Disease"):

    result = predict_chronic_disease(
        age,
        bp,
        sg,
        al,
        hemo,
        sc,
        htn,
        dm,
        cad,
        appet,
        pc
    )

    if result == 0:

        st.error(
            "⚠️ Prediction: The patient is likely to have Chronic Kidney Disease."
        )

    else:

        st.success(
            "✅ Prediction: The patient is NOT likely to have Chronic Kidney Disease."
        )

# ---------------------------------------
# Sample Data
# ---------------------------------------

st.divider()

with st.expander("📋 Sample Data (Kidney Disease = YES)"):
    st.code("""
        62,80,1.010,2,9.6,1.8,no,yes,no,poor,normal
        
        48,70,1.005,4,11.2,3.8,yes,no,no,poor,abnormal
        """)
with st.expander("📋 Sample Data (Kidney Disease = NO)"):
    st.code("""
        55,80,1.020,0,15.7,0.5,no,no,no,good,normal
        
        42,70,1.025,0,16.5,1.2,no,no,no,good,normal
        """)

st.write("<h3>We can use all these values to check results.</h3>",unsafe_allow_html=True)
st.write("""<div><ol>
    <li>Blood Sugar Level</li>
    <li>Red Blood Cells</li>
    <li>Pus Cell Clumps</li>
    <li>Bacteria in Urine</li>
    <li>Random Blood Glucose</li>
    <li>Blood Urea</li>
    <li>Sodium Level</li>
    <li>Potassium Level</li>
    <li>Packed Cell Volume (PCV)</li>
    <li>White Blood Cell Count (WBC)</li>
    <li>Red Blood Cell Count (RBC)</li>
    <li>Pedal Edema (Swelling of Feet)</li>
    <li>Anemia</li>
</ol></div>""",unsafe_allow_html=True)
