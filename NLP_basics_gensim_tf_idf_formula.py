# Import Dictionary
from gensim.corpora.dictionary import Dictionary
from collections import defaultdict
import itertools
import re
from nltk.tokenize import regexp_tokenize
# Create a Dictionary from the articles: dictionary
holy_grail = """GALAHAD: I seek the Grail.
BRIDGEKEEPER: What is your favorite color?
GALAHAD: Blue.  No yel-- auuuuuuuugh!
BRIDGEKEEPER: Hee hee heh.  Stop!  What is your name?
ARTHUR: It is Arthur, King of the Britons.
BRIDGEKEEPER: What is your quest?
ARTHUR: To seek the Holy Grail.
BRIDGEKEEPER: What is the air-speed velocity of an unladen swallow?
ARTHUR: What do you mean?  An African or European swallow?
BRIDGEKEEPER: Huh?  I-- I don't know that!  Auuuuuuuugh!
BEDEVERE: How do know so much about swallows?"""

lines = holy_grail.split('\n')
print(lines)
# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]
print(lines)
# Tokenize each line: tokenized_lines
pattern_words = "\w+"
tokenized_lines = [regexp_tokenize(s,pattern_words) for s in lines]
dictionary = Dictionary(tokenized_lines)
print(dictionary)
# Select the id for "computer": computer_id
computer_id = dictionary.token2id.get("Grail")
print(computer_id)
# Use computer_id with the dictionary to print the word
print(dictionary.get(computer_id))

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in tokenized_lines]

# Print the first 10 word ids with their frequency counts from the fifth document
print(corpus[4][:10])

# Save the fifth document: doc
doc = corpus[4]

# Sort the doc for frequency: bow_doc
bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)

# Print the top 5 words of the document alongside the count
for word_id, word_count in bow_doc[:5]:
    print(dictionary.get(word_id), word_count)

# Create the defaultdict: total_word_count
total_word_count = defaultdict(int)
for word_id, word_count in itertools.chain.from_iterable(corpus):
    total_word_count[word_id] += word_count

# Create a sorted list from the defaultdict: sorted_word_count
sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1], reverse=True)

# Print the top 5 words across all documents alongside the count
for word_id, word_count in sorted_word_count[:5]:
    print(dictionary.get(word_id), word_count)


# TI_ DIF
from gensim.models.tfidfmodel import TfidfModel
# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[doc]

# Print the first five weights
print(tfidf_weights[:5])


# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[doc]

# Print the first five weights
print(tfidf_weights[:5])

# Sort the weights from highest to lowest: sorted_tfidf_weights
sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)

print(sorted_tfidf_weights)
# Print the top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary.get(term_id), weight)