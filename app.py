import streamlit as st
import google.generativeai as genai
import os

# Read Google API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API Key not found. Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="Scholarship Eligibility Analyzer")
st.title("🎓 Scholarship Eligibility Analyzer")

prompt_template = """
Based on the following student information, evaluate their scholarship eligibility.
List potential scholarships and provide personalized application guidance.

Student Info:
{student_details}
"""

user_input = st.text_area("Enter student details:", height=200, placeholder="E.g., 12th grade, GPA 3.9, Female, income $25,000, basketball, disability: Yes...")

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter student details.")
    else:
        prompt = prompt_template.format(student_details=user_input)
        with st.spinner("Analyzing eligibility..."):
            response = model.generate_content(prompt)
            st.success("Scholarship Suggestions:")
            st.markdown(response.text)
