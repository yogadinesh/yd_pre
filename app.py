import streamlit as st
from transformers import pipeline

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Cybersecurity Incident Analyzer",
    page_icon="🔐",
    layout="centered"
)

# ---------------- TITLE ----------------

st.title("🔐YOGADINESH APP of GenAI Cybersecurity Incident Analyzer")

st.write(
    "Analyze cybersecurity logs using Generative AI and Chain-of-Thought Prompting"
)

# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():

    generator = pipeline(
        "text2text-generation",
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

# ---------------- ANALYZE BUTTON ----------------

if st.button("Analyze Incident"):

    # Empty input check
    if logs.strip() == "":

        st.warning("⚠️ Please enter security logs.")

    else:

        # Prompt Engineering
        prompt = f"""
You are an expert cybersecurity SOC analyst.

Analyze the following security logs step-by-step.

Tasks:
1. Identify suspicious activities
2. Detect attack patterns
3. Determine severity level
4. Identify affected systems
5. Suggest mitigation strategies
6. Recommend prevention methods

Security Logs:
{logs}

Generate a professional cybersecurity incident report.
"""

        # Loading Spinner
        with st.spinner("🔍 Analyzing Incident..."):

            response = generator(
                prompt,
                max_length=300
            )

            result = response[0]["generated_text"]

        # Display Output
        st.subheader("📊 Incident Analysis Report")

        st.success("✅ Analysis Completed")

        st.write(result)
