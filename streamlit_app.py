import streamlit as st
import pandas as pd
import joblib

modelo = joblib.load("model/knn_model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.set_page_config(
    page_title="Saúde +",
    page_icon="❤️",
    layout="centered"
)

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background: radial-gradient(circle at top, #0b1220, #0f172a, #020617);
}

.block-container{
    max-width: 800px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1,h2,h3,p,label{
    color:white !important;
}

.header{
    text-align:center;
    margin-bottom:30px;
}

.header h1{
    font-size:2.8rem;
    font-weight:800;
    background: linear-gradient(90deg,#ff4b4b,#ffb3b3);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.header p{
    color:#cbd5e1;
    font-size:1.05rem;
}

.card{
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    margin-bottom:20px;
}

div[data-baseweb="input"]{
    border-radius:12px;
}

.stButton button{
    width:100%;
    height:55px;
    border-radius:14px;
    font-size:18px;
    font-weight:bold;
    background: linear-gradient(90deg,#ff4b4b,#ff6b6b);
    color:white;
    border:none;
    box-shadow: 0 10px 25px rgba(255,75,75,0.25);
}

.stButton button:hover{
    transform: scale(1.01);
}

.result{
    margin-top:25px;
    padding:25px;
    border-radius:20px;
    text-align:center;
    animation: fadeIn 0.6s ease-in-out;
}

@keyframes fadeIn{
    from {opacity:0; transform: translateY(10px);}
    to {opacity:1; transform: translateY(0);}
}

.metric{
    font-size:2.5rem;
    font-weight:800;
}

.stSlider > div{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>❤️ Saúde +</h1>
    <p>Inteligência Artificial para predição de risco cardíaco</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📋 Informações do Paciente")

age = st.slider("Idade", 18, 100, 50)

sex = st.radio("Sexo", ["Feminino", "Masculino"], horizontal=True)

cholesterol = st.number_input("Colesterol (mg/dl)", 0, 600, 200)

fasting_bs = st.radio("Glicemia > 120 mg/dl?", ["Não", "Sim"], horizontal=True)

exercise_angina = st.radio("Angina durante exercício?", ["Não", "Sim"], horizontal=True)

st.divider()

st.subheader("🩺 Exames Clínicos")

resting_bp = st.number_input("Pressão arterial (mmHg)", 0, 250, 120)

max_hr = st.number_input("Frequência cardíaca máxima", 0, 250, 150)

oldpeak = st.number_input("Alteração ST (Oldpeak)", 0.0, 6.0, 0.0, step=0.1)

chest_pain = st.selectbox("Dor no peito", ["ASY", "ATA", "NAP", "TA"])

resting_ecg = st.selectbox("ECG em repouso", ["LVH", "Normal", "ST"])

st_slope = st.selectbox("Inclinação ST", ["Down", "Flat", "Up"])

st.markdown('</div>', unsafe_allow_html=True)

if st.button("🔍 Analisar Risco Cardíaco"):

    X_input = pd.DataFrame([{
    "Age": age,
    "RestingBP": resting_bp,
    "Cholesterol": cholesterol,
    "FastingBS": 1 if fasting_bs == "Sim" else 0,
    "MaxHR": max_hr,
    "Oldpeak": oldpeak,
    "Sex_M": 1 if sex == "Masculino" else 0,
    "ChestPainType_ATA": 1 if chest_pain == "ATA" else 0,
    "ChestPainType_NAP": 1 if chest_pain == "NAP" else 0,
    "ChestPainType_TA": 1 if chest_pain == "TA" else 0,
    "RestingECG_Normal": 1 if resting_ecg == "Normal" else 0,
    "RestingECG_ST": 1 if resting_ecg == "ST" else 0,
    "ExerciseAngina_Y": 1 if exercise_angina == "Sim" else 0,
    "ST_Slope_Flat": 1 if st_slope == "Flat" else 0,
    "ST_Slope_Up": 1 if st_slope == "Up" else 0
}])

    X_scaled = scaler.transform(X_input)

    pred = modelo.predict(X_scaled)[0]

    st.markdown("---")

    if pred == 1:

        st.markdown("""
        <div style="
            background:#7f1d1d;
            padding:30px;
            border-radius:20px;
            text-align:center;
            border:2px solid #ef4444;
            color:white;
            font-size:28px;
            font-weight:bold;
        ">
            ⚠️ ALTO RISCO DE DOENÇA CARDÍACA
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div style="
            background:#14532d;
            padding:30px;
            border-radius:20px;
            text-align:center;
            border:2px solid #22c55e;
            color:white;
            font-size:28px;
            font-weight:bold;
        ">
            ✅ BAIXO RISCO DE DOENÇA CARDÍACA
        </div>
        """, unsafe_allow_html=True)