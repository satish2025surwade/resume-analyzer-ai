from pdfminer.high_level import extract_text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills import role_skills 
import nltk
import string

nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords

# Extract text from PDF
def extract_text_from_pdf(file):
    return extract_text(file)

# Clean text
def preprocess(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    words = [w for w in words if w not in stopwords.words('english')]
    words = [w for w in words if w not in string.punctuation]
    return " ".join(words)

# Extract skills
def extract_skills(text, skills_db):
    found = []
    for skill in skills_db:
        if skill in text:
            found.append(skill)
    return found

# Job Matching Score
def match_score(resume_text, job_desc):
    cv = CountVectorizer()
    vectors = cv.fit_transform([resume_text, job_desc])
    score = cosine_similarity(vectors)[0][1]
    return round(score * 100, 2)

# Missing Skills
  # <-- add this import

def extract_skills(text, selected_role):
    skills_list = role_skills[selected_role]
    
    found = []
    for skill in skills_list:
        if skill in text:
            found.append(skill)
    
    return found, skills_list