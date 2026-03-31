import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyBp4rq_wPx4KiuBEN4sK5z7_bv-tMd2tlc")
st.set_page_config(page_title="AI Resume Builder",layout="wide")
st.subheader("Resume Generator")
col1,col2,col3,col4,col5=st.columns(5)
with col1:
    name = st.text_input("Enter your name:")
with col2:
    age = st.number_input("Enter the age:",min_value=18,max_value=65, format="%d")
with col3:
    phone =st.text_input("Enter phone number: ")
with col4:
    skills =st.text_input("Enter your skills: ")
with col5:
    experience =st.text_area("Enter your experience: ")
def resume_generator(name,age,phone,skills,experience):
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    prompt=(f"""
        Create a professional ATS-friendly resume.

    Name: {name}
    Age: {age}
    Phone: {phone}
    Skills: {skills}
    Experience: {experience}

    Format STRICTLY:
    1. Summary
    2. Skills (bullet points)
    3. Experience (bullet points)
    4. Education

    Do NOT give explanations.
    Only output resume.
    """)
    response=model.generate_content(prompt)
    output=response.text
    def clean(text):
        text=text.encode("Latin-1","ignore").decode("Latin-1")
        return text
    cleaned=clean(output)
    st.markdown("Generated Resume >>")
    st.markdown(
        f"<div style='background:##FFFFFF;padding:20px;border-radius:10px'>{cleaned}<\div>",
        unsafe_allow_html=True
    )
    from fpdf import FPDF
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=16)
    for line in cleaned.split("\n"):
        pdf.cell(200,10,txt=line,ln=True)
    pdf.output=pdf.output(dest='S').encode("Latin-1")
    st.download_button(
        label="📄 Download Resume in PDF",
        data=pdf.output,
        file_name="Resume.pdf",
        mime="application/pdf"
    )
if st.button("Generate Resume"):
    if len(phone)!=10:
        st.error("Enter a valid phone number")
    resume_generator(name,age,phone,skills,experience)


    