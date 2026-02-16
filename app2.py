import streamlit as st
from hf_summarizer import summarizer
from PyPDF2 import PdfReader  

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Text Summarizer")
st.markdown("Summarize long articles into short, clear insights using NLP.")
st.divider()

uploaded_file = st.file_uploader("Upload a TXT or PDF file", type=["txt", "pdf"])

text = ""

if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        text = str(uploaded_file.read(), "utf-8")
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"

text = st.text_area("📄 Text Content", text, height=300)

def get_summary_lengths(text):
    words = len(text.split())
    if words <= 100:
        return 30, 60   
    elif 100 < words <= 500:
        return 60, 150  
    elif 500 < words <= 1000:    
        return 80, 160 
    else:
        return 100, 200

if st.button("✨ Summarize"):
    if text.strip() != "":
        min_len, max_len = get_summary_lengths(text)
        with st.spinner("Generating summary..."):
            summary = summarizer(text, max_length=max_len, min_length=min_len)
            summary_text = summary[0]['summary_text']

        st.subheader("📝 Summary")
        st.success("Summary generated!")
        st.write(summary_text)
    else:
        st.warning("Please enter text first")
