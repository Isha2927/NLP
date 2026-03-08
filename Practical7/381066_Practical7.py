import nltk
from nltk.util import ngrams
from collections import defaultdict, Counter
import random

# Sample corpus
text = """
machine learning is amazing
machine learning is powerful
machine learning helps computers learn
natural language processing is part of machine learning
"""

# Tokenization
tokens = nltk.word_tokenize(text.lower())

# Create trigram model
n = 3
ngrams_list = list(ngrams(tokens, n))

# Dictionary for storing predictions
model = defaultdict(list)

for w1, w2, w3 in ngrams_list:
    model[(w1, w2)].append(w3)

# Convert lists to frequency counts
model_freq = {k: Counter(v) for k, v in model.items()}

# Function for auto complete
def autocomplete(text):
    words = text.lower().split()
    
    if len(words) < 2:
        return "Enter at least two words"
    
    key = (words[-2], words[-1])
    
    if key in model_freq:
        predictions = model_freq[key].most_common(3)
        return [word for word, count in predictions]
    else:
        return "No prediction found"

# Test the model
user_input = input("Enter a sentence: ")
print("Suggested words:", autocomplete(user_input))