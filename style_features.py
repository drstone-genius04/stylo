import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
import textstat
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')

def uses_semicolon(text):
    return ';' in text

def capitalizes_after_punctuation(text, punctuation):
    tokenizer = PunktSentenceTokenizer()
    sentences = tokenizer.tokenize(text)
    capitalized = [sentence for sentence in sentences if sentence.strip() and sentence.strip()[0].isupper()]
    return len(capitalized) / len(sentences) * 100 if sentences else 0

def vocabulary_grade_level(text):
    return textstat.text_standard(text, float_output=False)

def check_paragraph_structure(text):
    paragraphs = text.split('\n\n')
    average_sentences_per_paragraph = sum(len(sent_tokenize(p)) for p in paragraphs) / len(paragraphs) if paragraphs else 0
    return average_sentences_per_paragraph

def average_sentence_length(text):
    sentences = sent_tokenize(text)
    avg_length = sum(len(word_tokenize(sentence)) for sentence in sentences) / len(sentences) if sentences else 0
    return avg_length

def lexical_diversity(text):
    words = word_tokenize(text)
    unique_words = set(words)
    return len(unique_words) / len(words) if words else 0

def average_word_length(text):
    words = word_tokenize(text)
    return sum(len(word) for word in words) / len(words) if words else 0

def count_passive_voice(text):
    sentences = nltk.sent_tokenize(text)
    passive_count = 0
    for sentence in sentences:
        tagged_sent = pos_tag(word_tokenize(sentence))
        for i, word in enumerate(tagged_sent):
            if word[1] == 'VBN':
                if i > 0 and tagged_sent[i-1][1] in ['VB', 'VBG', 'VBD', 'VBP', 'VBZ']:
                    passive_count += 1
    return passive_count

# Implement more sophisticated features as needed
