import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Cybersecurity Incident Analyzer")

st.title("🔐 GenAI Cybersecurity Incident Analyzer")

@st.cache_resource
def load_model():

    generator = pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

    return generator

generator = load_model()

logs = st.text_area("Enter Security Logs")

if st.button("Analyze Incident"):

    prompt = f"""
    Analyze these cybersecurity logs.

    Logs:
    {logs}

    Identify:
    - suspicious activity
    - attack type
    - severity
    - mitigation
    """

    with st.spinner("Analyzing..."):

        response = generator(
            prompt,
            max_length=300
        )

    result = response[0]["generated_text"]

    st.write(result)
