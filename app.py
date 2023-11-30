import streamlit as st
import PyPDF2
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import nltk

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Title of the app
st.title('Author Comparison App')

# Function to read PDF files
def read_pdf(file):
    pdf_file_obj = PyPDF2.PdfFileReader(file)
    text = ''
    for page_num in range(pdf_file_obj.numPages):
        page_obj = pdf_file_obj.getPage(page_num)
        text += page_obj.extractText()
    return text

# Text area for the first author's text
author1_text = st.text_area('Enter the first author\'s text here')

# File uploader for the first author's PDF
author1_file = st.file_uploader('Upload the first author\'s PDF', type='pdf')

# If a PDF is uploaded, read the text from it
if author1_file is not None:
    author1_text = read_pdf(author1_file)

# Text area for the second author's text
author2_text = st.text_area('Enter the second author\'s text here')

# File uploader for the second author's PDF
author2_file = st.file_uploader('Upload the second author\'s PDF', type='pdf')

# If a PDF is uploaded, read the text from it
if author2_file is not None:
    author2_text = read_pdf(author2_file)

# Function to compare the writing styles using the Delta Method
def preprocess_text(text):
    """Preprocess a text: lower case, remove punctuation and stop words."""
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in string.punctuation]
    tokens = [token for token in tokens if token not in stop_words]
    return ' '.join(tokens)

def compare_styles(text1, text2):
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)

    # Vectorize texts into Count Vectors
    vectorizer = CountVectorizer().fit([text1, text2])
    vectors = vectorizer.transform([text1, text2])

    # Calculate cosine similarity between the vectors
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])

    return {"Similarity": similarity[0][0]}


# Button to compare the writing styles
if st.button('Compare'):
    # Compare the writing styles and display the results
    if author1_text and author2_text:
        comparison_results = compare_styles(author1_text, author2_text)
        st.write('The comparison results are:', str(math.ceil(comparison_results['Similarity']*100)) + "% Similarity")
        # st.bar_chart(comparison_results)