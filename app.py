import streamlit as st
from transformers import pipeline

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Cybersecurity Incident Analyzer",
    page_icon="🔐"
)

# ---------------- TITLE ----------------

st.title("🔐 GenAI Cybersecurity Incident Analyzer")

st.write("Analyze cybersecurity logs using AI")

# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():

    model = pipeline(
        task="text2text-generation",
        model="google/flan-t5-base"
    )

    return model

# Create generator object
generator = load_model()

# ---------------- USER INPUT ----------------

logs = st.text_area(
    "Enter Security Logs",
    height=250,
    placeholder="Paste security logs here..."
)

# ---------------- BUTTON ----------------

if st.button("Analyze Incident"):

    if logs.strip() == "":

        st.warning("⚠️ Please enter security logs.")

    else:

        # Prompt
        prompt = f"""
Analyze the following cybersecurity logs.

Logs:
{logs}

Provide:
1. Suspicious activities
2. Attack type
3. Severity
4. Mitigation
5. Prevention
"""

        # AI Processing
        with st.spinner("🔍 Analyzing Incident..."):

            response = generator(
                prompt,
                max_length=200
            )

            result = response[0]["generated_text"]

        # Output
        st.subheader("📊 Incident Analysis Report")

        st.success("✅ Analysis Completed")

        st.write(result)
