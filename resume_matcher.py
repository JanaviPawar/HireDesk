import os
import fitz  # PyMuPDF for PDFs
import docx
from sentence_transformers import SentenceTransformer, util

# Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2')


# Function to extract text from PDFs and DOCX
def load_resume_text(file_path):
    text = ""
    if file_path.lower().endswith(".pdf"):
        try:
            with fitz.open(file_path) as doc:
                for page in doc:
                    text += page.get_text()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    elif file_path.lower().endswith(".docx"):
        try:
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                text += para.text + "\n"
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    return text


# Function to calculate similarity between job description and resumes
def calculate_similarity(job_description, resumes_folder):
    """Compute semantic similarity between job description and each resume"""
    job_embedding = model.encode(job_description, convert_to_tensor=True)

    results = []

    for file in os.listdir(resumes_folder):
        path = os.path.join(resumes_folder, file)
        resume_text = load_resume_text(path)

        if not resume_text.strip():
            continue

        resume_embedding = model.encode(resume_text, convert_to_tensor=True)
        similarity_score = util.cos_sim(job_embedding, resume_embedding).item() * 100
        results.append((file, round(similarity_score, 2)))

    results.sort(key=lambda x: x[1], reverse=True)
    return results
