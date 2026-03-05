import pandas as pd

# Step 1: Load the CSV
csv_path = "C:/Users/YourName/Downloads/resume_dataset.csv"  # change to your CSV path
df_resumes = pd.read_csv(csv_path)

# Inspect the first few rows
print(df_resumes.head())
print("Columns:", df_resumes.columns)

# Step 2: Extract the resume text column
resumes_text = df_resumes['Resume_Text'].tolist()  # replace 'Resume_Text' with your actual column name
print(f"Total resumes loaded: {len(resumes_text)}")
print("Sample resume text:\n", resumes_text[0])
