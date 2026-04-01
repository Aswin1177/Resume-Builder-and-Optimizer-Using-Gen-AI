import streamlit as st
import google.generativeai as genai
genai.configure(api_key="API_KEY")
st.markdown("<h1 style= 'text-align: center;'>AI Resume Builder</h1>",unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Create ATS-Friendly Resumes Instantly</p>",unsafe_allow_html=True)
st.divider()
st.subheader("Generate Resume")
st.set_page_config(layout='wide')
col1,col2,col3=st.columns(3)
with st.container():
    st.markdown("""
                <div style="background:#1e1e1e;padding:20px;border-radius:12px;margin-bottom;10px"></div>""",unsafe_allow_html=True)
with col1:
    st.markdown("PERSONAL INFORMATION :")
    name=st.text_input("Enter the name")
    phone=st.text_input("Enter the phone number")
    email=st.text_input("Enter the e-mail id")
with col2:
    st.markdown("SKILLS, EXPERIENCE AND PROJECT :")
    skills=st.text_area("Enter the skills",height=150)
    experience=st.text_area("Enter the Experience",height=200)
    projects=st.text_area("Enter the projects",height=200)
with col3:
    st.markdown("EDUCATION AND LANGUAGES KNOWN :")
    education=st.text_area("Enter the Education",height=150)
    language=st.text_input("Enter the languages known")
job=st.checkbox("Optimize resume to align with specific job role")
if job:
    job_role=st.text_input("Enter the job role :")
    job_description=st.text_area("Enter the job description",height=200)
company=st.checkbox("Optimize resume to align with specific company")
if company:
    company_name=st.text_input("Enter the company name and place :")
normal=st.checkbox("Optimize Resume in ATS-friendly structure")
if normal:
    st.write("Resume is being generated")
def generate_resume(name,phone,email,skills,experience,projects,education,language,job,job_description,job_role,company,company_name,normal):
    model=genai.GenerativeModel("models/gemini-2.0-flash")
    if job:
        prompt=(f"""You are a professional resume writer.

            Rewrite and IMPROVE the following resume.

            DO NOT copy text directly.
            DO:
            - Rephrase content
            - Add strong action verbs
            - Make it 90%+ ATS optimized
            - Add measurable impact where possible
            - Improve clarity and professionalism
            - Optimize the keywords to match the skills mentioned in specified job description and job role

            Name: {name}
            Phone number: {phone}
            email: {email}
            skills: {skills}
            experience: {experience}
            projects: {projects}
            education: {education}
            language: {language}
            job description: {job_description}
            job role: {job_role}

            Strictly follow this format:

            Personal details
            Professional Summary
            Professional Experience
            Skills
            Education

            Output format:

            NAME
            CONTACT

            SUMMARY
            [improved paragraph]

            SKILLS
            • ...

            EXPERIENCE
            • Rewrite each point with impact

            EDUCATION
            ...

            final Resume should fit in maximum one page pdf
            Do not use bold text and unwanted symbols
            Only output the final resume.
            """)
        prompt2=(f"""
            You are an expert AI career coach, resume reviewer, and technical interviewer.

            Analyze the candidate's resume with details provided below and compare it with the job description.
                 
             Name: {name}
            Phone number: {phone}
            email: {email}
            skills: {skills}
            experience: {experience}
            projects: {projects}
            education: {education}
            language: {language}
            job description: {job_description}
            job role: {job_role}
    
            JOB DESCRIPTION:
            {job_description}

            Perform the following tasks:

            ### 1. SKILL EXTRACTION
            - Extract key technical and soft skills required from the job description
            - Extract candidate's skills from the resume

            ---

            ### 2. SKILL GAP ANALYSIS
            - Compare both skill sets
            - Identify missing or weak skills
            - Categorize them into:
            • Critical (must-have)
            • Important (good-to-have)
            • Optional (bonus)

            ---

            ### 3. MATCH SCORE
            - Give a percentage match score (0–100%)
            - Briefly explain why this score was given

            ---

            ### 4. RESUME IMPROVEMENT SUGGESTIONS
            - Suggest improvements to make the resume ATS-friendly
            - Suggest how to rewrite experience with measurable impact
            - Highlight missing keywords to include

            ---

            ### 5. LEARNING ROADMAP (VERY IMPORTANT)
            For EACH missing skill:
            - Suggest FREE resources (YouTube, documentation, courses)
            - Provide:
            • Resource name
            • Platform (YouTube, Coursera, Docs, etc.)
            • Direct learning approach (what exactly to learn)
            • Estimated time for an INTERMEDIATE learner (in days/weeks)
            - Keep it practical and fast-track focused

            ---

            ### 6. INTERVIEW PREPARATION
            For the TOP missing or important skills:
            - Provide 3–5 interview questions per skill
            - Provide CLEAR and concise answers
            - Focus on real interview-level questions (not basic definitions)

            ---

            ### 7. FINAL OUTPUT FORMAT (STRICT)

            Return output in this structured format:

            -------------------------
            MATCH SCORE:
            XX%

            -------------------------
            SKILL GAP:

            Critical:
            - ...

            Important:
            - ...

            Optional:
            - ...

            -------------------------
            LEARNING PLAN:

            Skill: ___
            - Resource:
            - Platform:
            - Time to Learn:
            - What to Focus:

            (repeat for each skill)

            -------------------------
            RESUME IMPROVEMENTS:
            - ...

            -------------------------
            INTERVIEW QUESTIONS:

            Skill: ___
            Q1:
            A:

            Q2:
            A:

            -------------------------

            Do NOT include unnecessary explanations.
            Be precise, structured, and actionable.
            """)
    elif(company):
        prompt=(f"""You are a professional resume writer.

            Rewrite and IMPROVE the following resume.

            DO NOT copy text directly.
            DO:
            - Rephrase content
            - Add strong action verbs
            - Make it 90%+ ATS optimized
            - Add measurable impact where possible
            - Improve clarity and professionalism
            - Optimize the keywords to match the skills that the specified company highly focuses on

            Name: {name}
            Phone number: {phone}
            email: {email}
            skills: {skills}
            experience: {experience}
            projects: {projects}
            education: {education}
            language: {language}
            company: {company_name}

            Strictly follow this format:

            Personal details
            Professional Summary
            Professional Experience
            Skills
            Education

            Output format:

            NAME
            CONTACT

            SUMMARY
            [improved paragraph]

            SKILLS
            • ...

            EXPERIENCE
            • Rewrite each point with impact

            EDUCATION
            ...

            final Resume should fit in maximum one page pdf
            Do not use bold text and unwanted symbols
            Only output the final resume.
            """)
    elif(job and company):
        prompt=(f"""You are a professional resume writer.

            Rewrite and IMPROVE the following resume.

            DO NOT copy text directly.
            DO:
            - Rephrase content
            - Add strong action verbs
            - Make it 90%+ ATS optimized
            - Add measurable impact where possible
            - Improve clarity and professionalism
            - Optimize the keywords to match the skills mentioned in specified job description and job role
            - Optimize the keywords to match the skills that the specified company highly focuses on

            Name: {name}
            Phone number: {phone}
            email: {email}
            skills: {skills}
            experience: {experience}
            projects: {projects}
            education: {education}
            language: {language}
            job description: {job_description}
            job role: {job_role}
            company name: {company_name}

            Strictly follow this format:

            Personal details
            Professional Summary
            Professional Experience
            Skills
            Education

            Output format:

            NAME
            CONTACT

            SUMMARY
            [improved paragraph]

            SKILLS
            • ...

            EXPERIENCE
            • Rewrite each point with impact

            EDUCATION
            ...

            final Resume should fit in maximum one page pdf
            Do not use bold text and unwanted symbols
            Only output the final resume.
            """)
    elif((normal and job)or (normal and company)):
        st.error("normal cannot be combined with other options")
    else:
        prompt=(f"""You are a professional resume writer.

            Rewrite and IMPROVE the following resume.

            DO NOT copy text directly.
            DO:
            - Rephrase content
            - Add strong action verbs
            - Make it 90%+ ATS optimized
            - Add measurable impact where possible
            - Improve clarity and professionalism

            Name: {name}
            Phone number: {phone}
            email: {email}
            skills: {skills}
            experience: {experience}
            projects: {projects}
            education: {education}
            language: {language}

            Strictly follow this format:

            Personal details
            Professional Summary
            Professional Experience
            Skills
            Education

            Output format:

            NAME
            CONTACT

            SUMMARY
            [improved paragraph]

            SKILLS
            • ...

            EXPERIENCE
             Rewrite each point with impact

            EDUCATION
            ...

            final Resume should fit in maximum one page pdf
            Do not use bold text and unwanted symbols
            Only output the final resume.
        """)
    response=model.generate_content(prompt)
    st.write("Please wait..The resume is being generated\n")
    response2=model.generate_content(prompt2)
    output2=response2.text
    output=response.text
    def clean(text):
        text=text.encode("Latin-1","ignore").decode("Latin-1")
        return text
    cleaned_output=clean(output)
    cleaned_output2=clean(output2)
    st.markdown("Generated Resume:\n")
    st.markdown("*****************************")
    st.markdown(f"<div background:##FFFFFF;padding:20px;border-radius:10px>{cleaned_output}</div>",
                unsafe_allow_html=True)
    st.markdown("*****************************")
    st.markdown("\n","Resume has been analyzed thoroughly and we found some helpfull features for you:\n")
    st.markdown("******************************")
    st.markdown(f"<div background:##FFFFFF;padding:20px;border-radius:10px>{cleaned_output2}</div>",
                unsafe_allow_html=True)   
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    def generate_resume_pdf(text):
        doc = SimpleDocTemplate(
            "resume.pdf",
            pagesize=A4,
            rightMargin=40,
            leftMargin=40,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()

        content = []

        for line in text.split("\n"):
            if line.strip() == "":
                content.append(Spacer(1, 10))
            elif line.isupper():  # headings
                content.append(Paragraph(f"<b>{line}</b>", styles["Heading3"]))
                content.append(Spacer(1, 8))
            else:
                content.append(Paragraph(line, styles["Normal"]))
                content.append(Spacer(1, 6))

        doc.build(content)
    generate_resume_pdf(cleaned_output)
    with open("resume.pdf","rb") as f:
        pdf=f.read()
    st.download_button(label="📄 Download PDF", data=pdf, file_name="Resume.pdf", mime="application/pdf")
if st.button("➡Generate Resume",use_container_width=True):
    if(len(phone)!=10):
        st.error("Enter a valid Indian mobile number")
    generate_resume(name,phone,email,skills,experience,projects,education,language,job,job_description,job_role,company,company_name,normal)
