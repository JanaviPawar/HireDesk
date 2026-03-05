import pandas as pd

# Path to your CSV file
csv_path = "C:/Users/Janhvi/Desktop/ai_resume_project/resume_dataset.csv"  # change this to your CSV path

# Load CSV
df_resumes = pd.read_csv(csv_path)

# Inspect the first few rows
print(df_resumes.head())
print("Columns:", df_resumes.columns)

# Extract resume text column
resumes_text = df_resumes['Resume_Text'].tolist()  # replace 'Resume_Text' with your actual column name
print(f"Total resumes loaded: {len(resumes_text)}")
print("Sample resume text:\n", resumes_text[0])
