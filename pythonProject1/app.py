import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
load_dotenv()  # load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
            max-width: 800px;
            margin: auto;
        }
        .title {
            font-size: 2.5rem;
            color: #2E8B57;
            text-align: center;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #555;
            text-align: center;
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            color: #2E8B57;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit app
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("<h3 class='title'>Resume Optimizer Pro</h3>", unsafe_allow_html=True)
st.markdown("<h5 class='subtitle'>Optimize your Resume to Maximum Visibility</h5>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Job Description Input
jd = st.text_area("Paste the Job Description (required)", help="Enter the job description here. This field is mandatory.")
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf", help="Please upload the resume in PDF format.")

submit = st.button("Submit")

if submit:
    if not jd:
        st.error("Job Description is required!")
    elif uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        filled_prompt = input_prompt.format(text=text, jd=jd)
        response = get_gemini_response(filled_prompt)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.error("Please upload the resume.")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Powered by Prabal Kumar</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
