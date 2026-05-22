import streamlit as st
from transformers import pipeline

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Cybersecurity Incident Analyzer",
    page_icon="🔐"
)

# ---------------- TITLE ----------------

st.title("🔐 GenAI Cybersecurity Incident Analyzer")

st.write(
    "Analyze cybersecurity logs using AI"
)

# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():

    generator = pipeline(
       task="text2text-generation"
        model="google/flan-t5-base"
    )

    return generator

generator = load_model()

# ---------------- USER INPUT ----------------

logs = st.text_area(
    "Enter Security Logs",
    height=250,
    placeholder="Paste cybersecurity logs here..."
)

# ---------------- BUTTON ----------------

if st.button("Analyze Incident"):

    if logs.strip() == "":

        st.warning("⚠️ Please enter security logs.")

    else:

        prompt = f"""
Cybersecurity Incident Report

Analyze these logs:

{logs}

Identify:
- suspicious activities
- attack type
- severity
- mitigation
- prevention
"""

        with st.spinner("🔍 Analyzing Incident..."):

            response = generator(
                prompt,
                max_length=200,
                num_return_sequences=1
            )

            result = response[0]["generated_text"]

        st.subheader("📊 Incident Analysis Report")

        st.success("✅ Analysis Completed")

        st.write(result)
