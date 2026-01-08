# =========================================================
# 🏥 BREAST CANCER PREDICTION – AI CAREERS FOR WOMEN (AICW)
# Developed under Edunet | Microsoft | SAP
# Author: Sanjana Mali
# =========================================================

import streamlit as st
import pandas as pd
import io
import os
from tensorflow.keras.models import load_model
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# -------------------- PATH SETUP --------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Breast Cancer AI | AICW",
    page_icon="🏥",
    layout="centered"
)

# -------------------- UI STYLING --------------------
st.markdown("""
<style>
.title { text-align:center; font-size:36px; font-weight:bold; color:#2c3e50; }
.subtitle { text-align:center; font-size:17px; color:#555; }
.card {
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 8px 20px rgba(0,0,0,0.15);
    margin-bottom:25px;
}
.result-good {
    background:linear-gradient(to right,#43cea2,#185a9d);
    color:white;padding:20px;border-radius:15px;
    font-size:22px;font-weight:bold;text-align:center;
}
.result-bad {
    background:linear-gradient(to right,#ff416c,#ff4b2b);
    color:white;padding:20px;border-radius:15px;
    font-size:22px;font-weight:bold;text-align:center;
}
.footer { text-align:center;color:#666;margin-top:30px;font-style:italic; }
</style>
""", unsafe_allow_html=True)

# -------------------- LOGOS --------------------
# -------------------- LOGOS CARD --------------------
# -------------------- LOGOS CARD --------------------
st.markdown("<div style='background:#f0f8ff; padding:20px; border-radius:18px; display:flex; justify-content:space-around; align-items:center; margin-bottom:25px;'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.image("assets/edunet.png", width=120)
with col2:
    st.image("assets/microsoft.png", width=120)
with col3:
    st.image("assets/sap.png", width=120)

st.markdown("</div>", unsafe_allow_html=True)



# -------------------- HEADER --------------------
st.markdown("<div class='title'>AI Careers for Women (AICW)</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>A National Initiative by Edunet Foundation<br>"
    "In Collaboration with Microsoft & SAP</div>",
    unsafe_allow_html=True
)

st.write("---")
st.markdown("<div class='title'>🏥 Breast Cancer Early Detection System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-Assisted Screening Tool for Hospitals & Clinics</div>", unsafe_allow_html=True)

# -------------------- LOAD MODEL --------------------
model = load_model("breastcancer_model.h5")

# -------------------- PDF FUNCTION --------------------
def generate_pdf(patient, result, confidence, df):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []
    elements.append(Paragraph("Edunet  Microsoft  SAP", styles['Title']))
    elements.append(Paragraph("Breast Cancer AI Screening Report", styles['Title']))
    elements.append(Paragraph(
        "Developed under AI Careers for Women (AICW) – Edunet Foundation "
        "in collaboration with Microsoft & SAP",
        styles['Italic']
    ))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Patient Details</b>", styles['Heading2']))
    elements.append(Paragraph(f"Name: {patient['name']}", styles['Normal']))
    elements.append(Paragraph(f"Age: {patient['age']}", styles['Normal']))
    elements.append(Paragraph(f"Patient ID: {patient['id']}", styles['Normal']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AI Screening Result</b>", styles['Heading2']))
    elements.append(Paragraph(f"Diagnosis: <b>{result}</b>", styles['Normal']))
    elements.append(Paragraph(f"Confidence Level: {confidence*100:.2f}%", styles['Normal']))
    elements.append(Spacer(1, 12))

    table_data = [["Feature", "Value"]]
    for col in df.columns:
        table_data.append([col.replace("_", " ").title(), str(df[col][0])])

    table = Table(table_data, colWidths=[260, 200])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elements.append(table)

    elements.append(Spacer(1, 12))
    elements.append(Paragraph(
        "Disclaimer: This AI-generated report is for screening assistance only. "
        "Final diagnosis must be confirmed by a certified medical professional.",
        styles['Italic']
    ))

    doc.build(elements)
    buffer.seek(0)
    return buffer

# -------------------- SIDEBAR --------------------
st.sidebar.title("👤 Patient Information")
patient_name = st.sidebar.text_input("Patient Name")
patient_age = st.sidebar.number_input("Age", 1, 120)
patient_id = st.sidebar.text_input("Patient ID")

# -------------------- INPUT FEATURES --------------------
st.markdown("<div class='card'><h3>🧪 Tumor Measurements</h3></div>", unsafe_allow_html=True)

def user_input():
    data = {}
    features = [
        'radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean',
        'compactness_mean','concavity_mean','concave points_mean','symmetry_mean','fractal_dimension_mean',
        'radius_se','texture_se','perimeter_se','area_se','smoothness_se',
        'compactness_se','concavity_se','concave points_se','symmetry_se','fractal_dimension_se',
        'radius_worst','texture_worst','perimeter_worst','area_worst','smoothness_worst',
        'compactness_worst','concavity_worst','concave points_worst','symmetry_worst','fractal_dimension_worst'
    ]
    for f in features:
        data[f] = st.number_input(f.replace("_"," ").title(), value=0.0)
    return pd.DataFrame(data, index=[0])

input_df = user_input()

# -------------------- PREDICTION --------------------
st.write("---")

if st.button("🔍 Predict Result", use_container_width=True):

    if patient_name == "" or patient_id == "":
        st.warning("Please enter patient details.")
        st.stop()

    prob = model.predict(input_df)[0][0]
    confidence = prob if prob >= 0.5 else 1 - prob

    if prob >= 0.5:
        result = "Malignant (Cancer Risk Detected)"
        st.markdown(f"<div class='result-bad'>❌ {result}<br>Confidence: {confidence*100:.2f}%</div>", unsafe_allow_html=True)
    else:
        result = "Benign (Low Risk)"
        st.markdown(f"<div class='result-good'>✅ {result}<br>Confidence: {confidence*100:.2f}%</div>", unsafe_allow_html=True)

    patient = {"name": patient_name, "age": patient_age, "id": patient_id}
    pdf = generate_pdf(patient, result, confidence, input_df)

    st.download_button(
        "📄 Download Medical Report (PDF)",
        data=pdf,
        file_name="Breast_Cancer_AI_Report.pdf",
        mime="application/pdf"
    )

# -------------------- FOOTER --------------------
st.markdown("<div class='footer'>Developed by Sanjana Mali | AI & Data Science</div>", unsafe_allow_html=True)
