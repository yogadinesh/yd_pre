import streamlit as st
from openai import OpenAI

# Page Config
st.set_page_config(page_title="Cybersecurity Incident Analyzer")

st.title("🔐 GenAI Cybersecurity Incident Analyzer")
st.write("Analyze cybersecurity logs using Chain-of-Thought Prompting")

# OpenAI Client
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# User Input
logs = st.text_area(
    "Enter Security Logs",
    height=250,
    placeholder="Paste security logs here..."
)

# Analyze Button
if st.button("Analyze Incident"):

    if logs.strip() == "":
        st.warning("Please enter security logs.")

    else:

        prompt = f"""
You are an expert cybersecurity SOC analyst.

Analyze the following logs step-by-step.

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

        with st.spinner("Analyzing Incident..."):

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional cybersecurity analyst."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3
            )

            result = response.choices[0].message.content

        st.subheader("📊 Incident Analysis Report")
        st.write(result)
