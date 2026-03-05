# 🤖 HireDesk — AI Resume Matcher

HireDesk is an AI-powered resume screening tool that ranks resumes based on their similarity to a given job description.

The system uses **Natural Language Processing (NLP)** with **Sentence Transformers** to compute semantic similarity between resumes and job descriptions.

---

## 🚀 Features

- Upload multiple resumes (.pdf or .docx)
- Upload a job description
- AI ranks resumes by match percentage
- View resume preview
- Download top N resumes
- Download top resumes as ZIP
- Chat with Resume (ask questions about a resume using AI)

---

## 🧠 Technologies Used

- Python
- Streamlit
- Sentence Transformers
- Hugging Face Transformers
- PyMuPDF
- python-docx

---

## 📂 Project Structure

HireDesk
│
├── app.py
├── resume_matcher.py
├── utils.py
├── sample_job_description.txt
├── sample_resumes
└── README.md


---

## ⚙️ Installation

Clone the repository
git clone https://github.com/JanaviPawar/HireDesk.git

Go into the project folder
cd HireDesk


Install dependencies


pip install -r requirements.txt


Run the application


streamlit run app.py

---

## 🧪 How It Works

1. The job description is converted into an embedding vector.
2. Each resume is converted into an embedding vector.
3. Cosine similarity is calculated between them.
4. Resumes are ranked based on similarity score.

---

## 📊 Future Improvements

- Resume skill extraction
- Automatic interview question generation
- Resume feedback system
- Resume summarization

---

## 👩‍💻 Author

**Janavi Pawar**

AI / Software Developer
