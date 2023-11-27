import streamlit as st
import style_features
import pandas as pd

st.title("Advanced Stylometric Analysis")

text1 = st.text_area("Enter Text 1", "Type or paste text here.")
text2 = st.text_area("Enter Text 2", "Type or paste text here.")

if st.button("Analyze Texts"):
    features1 = {
        "semicolon_usage": style_features.uses_semicolon(text1),
        "capitalization_after_full_stops": style_features.capitalizes_after_punctuation(text1, '.'),
        "vocabulary_grade": style_features.vocabulary_grade_level(text1),
        "lexical_diversity": style_features.lexical_diversity(text1),
        "average_sentence_length": style_features.average_sentence_length(text1),
        "average_word_length": style_features.average_word_length(text1),
        "passive_voice_usage": style_features.count_passive_voice(text1)
    }

    features2 = {
        "semicolon_usage": style_features.uses_semicolon(text2),
        "capitalization_after_full_stops": style_features.capitalizes_after_punctuation(text2, '.'),
        "vocabulary_grade": style_features.vocabulary_grade_level(text2),
        "lexical_diversity": style_features.lexical_diversity(text2),
        "average_sentence_length": style_features.average_sentence_length(text2),
        "average_word_length": style_features.average_word_length(text2),
        "passive_voice_usage": style_features.count_passive_voice(text2)
    }
    
    # Calculate a simple score for authorship likelihood
    numeric_features = ['semicolon_usage', 'capitalization_after_full_stops', 'lexical_diversity', 'average_sentence_length', 'average_word_length', 'passive_voice_usage']
    score = sum(abs(features1[key] - features2[key]) for key in numeric_features)
    authorship_likelihood = (1 - score / len(numeric_features)) * 100

# Displaying the results
    st.write("Feature Analysis for Text 1:", features1)
    st.write("Feature Analysis for Text 2:", features2)
# Creating DataFrames for visualization
    df_features1 = pd.DataFrame(list(features1.items()), columns=['Feature', 'Text 1'])
    df_features2 = pd.DataFrame(list(features2.items()), columns=['Feature', 'Text 2'])

    # Plotting the features
    st.bar_chart(df_features1.set_index('Feature'))
    st.bar_chart(df_features2.set_index('Feature'))

    # Fixing the likelihood percentage calculation
    numeric_differences = [abs(features1[key] - features2[key]) for key in numeric_features if isinstance(features1[key], (int, float)) and isinstance(features2[key], (int, float))]
    score = sum(numeric_differences)
    max_possible_score = len(numeric_features) * 100  # Assuming each feature can differ by up to 100%
    authorship_likelihood = max(0, min((1 - score / max_possible_score) * 100, 100))

    st.write("Likelihood of the Same Author:", f"{authorship_likelihood:.2f}%")