# 🤖 HireDesk — AI Resume Matcher

HireDesk is an AI-powered resume screening tool that ranks resumes based on their similarity to a given job description.

The system uses **Natural Language Processing (NLP)** with **Sentence Transformers** to compute semantic similarity between resumes and job descriptions.

---
## Live Demo

Streamlit App: https://hiredesk.streamlit.app/

⭐ If you like this project, give it a star!

## Screenshots

### Home Page

<img width="1919" height="958" alt="image" src="https://github.com/user-attachments/assets/12a787ba-8198-4cba-b591-3b431fd76b9b" />


### Resume Match Result

<img width="1919" height="1025" alt="image" src="https://github.com/user-attachments/assets/8468a668-42e0-44ca-80ba-fef367580cf4" />

<img width="1897" height="928" alt="image" src="https://github.com/user-attachments/assets/af2b1ef6-01e1-41b4-9751-68ee90b376fe" />

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
