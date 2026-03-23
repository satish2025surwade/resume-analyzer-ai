import streamlit as st
from utils import *
from skills import role_skills

# ✅ MUST be first
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# Header
st.markdown("""
# 🤖 AI Resume Analyzer  
### Improve your Resume with AI + ATS Score 🚀
""")

# 📥 Input Section
with st.container():
    st.subheader("📥 Upload Details")

    uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
    job_desc = st.text_area("📌 Paste Job Description")

    role = st.selectbox(
        "🎯 Select Job Role",
        list(role_skills.keys())
    )

# 🚀 Button
st.markdown("## 🚀 Start Analysis")
analyze_btn = st.button("Analyze Now", use_container_width=True)

# 🧠 Logic only runs when button clicked
if analyze_btn:
    if uploaded_file and job_desc:

        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            clean_resume = preprocess(resume_text)
            clean_job = preprocess(job_desc)

            resume_skills, total_skills = extract_skills(clean_resume, role)

            score = (len(resume_skills) / len(total_skills)) * 100
            missing = [skill for skill in total_skills if skill not in resume_skills]

        # 📊 Result UI
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 ATS Match Score")
            st.progress(int(score))
            st.write(f"### {round(score,2)}% Match")

            if score > 75:
                st.success("Excellent match 🚀")
            elif score > 50:
                st.warning("Good but can improve ⚡")
            else:
                st.error("Low match ❌ Improve your resume")

        with col2:
            st.subheader("🧠 Skills Found")
            st.write(resume_skills)

        st.subheader("❌ Missing Skills")
        st.write(missing)

        # 💡 Suggestions
        st.subheader("💡 Suggestions")
        if missing:
            for skill in missing:
                st.write(f"👉 Add **{skill}** to improve your resume")
        else:
            st.success("Your resume is well optimized!")

    else:
        st.warning("⚠️ Please upload resume and enter job description")

# Footer
st.markdown("---")
st.markdown("### 👨‍💻 Built by Satish Surwade 🚀")