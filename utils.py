import nltk
import string



# ✅ FIX ALL NLTK ISSUES
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from nltk.corpus import stopwords
from pdfminer.high_level import extract_text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills import role_skills


# 📄 Extract text from PDF
def extract_text_from_pdf(file):
    return extract_text(file)


# 🧹 Clean text
def preprocess(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    words = [w for w in words if w not in stopwords.words('english')]
    words = [w for w in words if w not in string.punctuation]
    return " ".join(words)


# 🧠 Extract skills (ROLE BASED)
def extract_skills(text, selected_role):
    skills_list = role_skills[selected_role]

    found = []
    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return found, skills_list


# 📊 Job Matching Score
def match_score(resume_text, job_desc):
    cv = CountVectorizer()
    vectors = cv.fit_transform([resume_text, job_desc])
    score = cosine_similarity(vectors)[0][1]
    return round(score * 100, 2)