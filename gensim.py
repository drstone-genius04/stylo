# gensim.py

from gensim import corpora, models, similarities
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def preprocess(text):
    lower = text.lower()
    no_punctuation = lower.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(no_punctuation)
    stopped_tokens = [w for w in tokens if not w in stopwords.words('english')]
    return stopped_tokens

def analyze_authorship(doc1, doc2):
    texts = [preprocess(doc1), preprocess(doc2)]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    
    # Using TF-IDF model for transformation
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    # Computing similarity matrix
    index = similarities.MatrixSimilarity(corpus_tfidf)
    sim = index[corpus_tfidf[0]]
    
    return sim[1]
