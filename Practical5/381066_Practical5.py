import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet as wn

synsets=wn.synsets("Sunshine",pos=wn.ADJ)
synonyms=set()

for syn in synsets:
    for lemma in syn.lemmas():
        synonyms.add(lemma.name())

print("Synonyms of 'Sunshine':", synonyms,"\n")
antonyms=set()
 
# Finding Antonyms
for syn in wn.synsets("sad",pos=wn.ADJ):
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.add(lemma.antonyms()[0].name())

print("Antonyms of 'sad':", antonyms,"\n")

# Finding Hypernyms 
hypernyms=set()

for syn in wn.synsets("dog",pos=wn.NOUN):
    for hypernym in syn.hypernyms():
        for lemma in hypernym.lemmas():
            hypernyms.add(lemma.name())

print("Hypernyms of 'dog':", hypernyms,"\n")

# Finding Hyponyms 
hyponyms=set()

for syn in wn.synsets("dog",pos=wn.NOUN):
    for hyponym in syn.hyponyms():
        for lemma in hyponym.lemmas():
            hyponyms.add(lemma.name())

print("Hyponyms of 'dog':", hyponyms,"\n")