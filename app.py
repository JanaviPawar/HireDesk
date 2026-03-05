import streamlit as st
import os
from resume_matcher import calculate_similarity, load_resume_text
import zipfile
from io import BytesIO
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

# Initialize QA model
@st.cache_resource
def load_qa_model():
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")
    model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad")
    return pipeline("question-answering", model=model, tokenizer=tokenizer)
qa_model = load_qa_model()

# Page setup
st.set_page_config(page_title="AI Resume Matcher", layout="wide")
st.title("🤖 AI Resume Matcher")
st.write("Upload your resumes and a job description — the AI will rank them by best match.")

# --- Upload sections ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("1️⃣ Upload Job Description")
    job_file = st.file_uploader("Upload a .txt file", type=["txt"])

with col2:
    st.subheader("2️⃣ Upload Resumes")
    uploaded_resumes = st.file_uploader(
        "Upload one or more resumes (.pdf or .docx)",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

# Option to choose top N resumes
top_n = st.number_input("Show top N resumes", min_value=1, value=3, step=1)

# Initialize session_state to store matching results
if "results" not in st.session_state:
    st.session_state.results = None
if "resume_text_dict" not in st.session_state:
    st.session_state.resume_text_dict = {}
if "temp_folder" not in st.session_state:
    st.session_state.temp_folder = None

# --- Match Resumes ---
if st.button("🚀 Match Resumes"):
    if not job_file or not uploaded_resumes:
        st.error("⚠️ Please upload both a job description and resumes first.")
    else:
        job_text = job_file.read().decode("utf-8")
        st.info("Analyzing resumes... please wait ⏳")

        # Save resumes to temp folder
        temp_folder = "temp_resumes"
        os.makedirs(temp_folder, exist_ok=True)
        st.session_state.temp_folder = temp_folder

        for resume in uploaded_resumes:
            with open(os.path.join(temp_folder, resume.name), "wb") as f:
                f.write(resume.read())

        # Calculate similarity
        results = calculate_similarity(job_text, temp_folder)

        if not results:
            st.warning("No resumes found or unable to extract text.")
        else:
            results.sort(key=lambda x: x[1], reverse=True)
            st.session_state.results = results[:top_n]

            # Load resume texts
            resume_text_dict = {}
            for name, score in st.session_state.results:
                resume_path = os.path.join(temp_folder, name)
                resume_text_dict[name] = load_resume_text(resume_path)
            st.session_state.resume_text_dict = resume_text_dict

# --- Display Top Resumes ---
if st.session_state.results:
    top_results = st.session_state.results
    st.success("✅ Matching complete!")
    st.subheader(f"🏆 Top {len(top_results)} Resumes:")

    for name, score in top_results:
        resume_text = st.session_state.resume_text_dict.get(name, "")
        resume_path = os.path.join(st.session_state.temp_folder, name)
        with st.expander(f"{name} → {score:.2f}% match"):
            st.write(f"**Match Score:** {score:.2f}%")
            if resume_text.strip():
                st.text_area("Resume Preview:", resume_text[:500], height=150)
            else:
                st.write("Cannot preview this file.")

            with open(resume_path, "rb") as f:
                resume_bytes = f.read()
            st.download_button(
                label="📄 Download this Resume",
                data=resume_bytes,
                file_name=name,
                mime="application/octet-stream"
            )

    # Download top N as ZIP
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for name, _ in top_results:
            resume_path = os.path.join(st.session_state.temp_folder, name)
            zip_file.write(resume_path, arcname=name)
    zip_buffer.seek(0)

    st.download_button(
        label=f"📥 Download Top {len(top_results)} Resumes as ZIP",
        data=zip_buffer,
        file_name=f"top_{len(top_results)}_resumes.zip",
        mime="application/zip"
    )

    # --- Chat with Resume ---
    st.subheader("💬 Chat with a Resume")
    selected_resume = st.selectbox("Select a resume to chat with:", [name for name, _ in top_results])
    resume_text = st.session_state.resume_text_dict.get(selected_resume, "")

    if "user_question" not in st.session_state:
        st.session_state.user_question = ""
    if "answer" not in st.session_state:
        st.session_state.answer = ""

    # Use a form to prevent reload on Enter
    with st.form(key="chat_form"):
        user_question = st.text_input(
            "Ask a question about this resume (e.g., skills, experience, education):",
            value=st.session_state.user_question
        )
        submit_button = st.form_submit_button("Ask")

        if submit_button and user_question.strip():
            if resume_text.strip():
                st.session_state.answer = qa_model(question=user_question, context=resume_text)["answer"]
            else:
                st.session_state.answer = "⚠️ No text available in this resume to answer the question."
            st.session_state.user_question = user_question

    # Display the answer
    if st.session_state.answer:
        st.markdown(f"**Answer:** {st.session_state.answer}")

# Cleanup temp folder when script ends (optional)
# You can add a button to clear cache if needed
