import nltk
from nltk.util import ngrams
from collections import defaultdict, Counter

# Sample dataset
text = """I love NLP and I love machine learning.
NLP is fun and machine learning is powerful.
I love coding and I love AI."""

# Preprocessing
tokens = nltk.word_tokenize(text.lower())

# Create bigrams
n = 2
bigrams = list(ngrams(tokens, n))

# Build model
model = defaultdict(Counter)

for w1, w2 in bigrams:
    model[w1][w2] += 1

# Function for prediction
def predict_next_word(word):
    if word in model:
        return model[word].most_common(3)
    else:
        return "No prediction available"

# Test
input_word = "love"
print(f"Next words for '{input_word}':")
print(predict_next_word(input_word))