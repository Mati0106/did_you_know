# Import necessary modules
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
nltk.download('punkt')
import re

scene_one ="""It's some of the text! Should you read it? I don't think so."""
print(scene_one)
# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[2])
print(tokenized_sent)
# # Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)

# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search(r"do", scene_one)
# # Print the start and end indexes of match
print(match.start(), match.end())


scene_one ="It's some of the text! [Should you read it] I don't think so."
# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = r"\[.*\]"

# Use re.search to find the first text in square brackets
print(re.search(pattern1, scene_one))


from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

tweets = ['smth smth2 #python #some_hash']
# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#\w+"
# Use the pattern on the first tweet in the tweets list
hashtags = regexp_tokenize(tweets[0], pattern1)
print(hashtags)
#

# Import the necessary modules
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer
# Write a pattern that matches both mentions (@) and hashtags
pattern2 = r"(@\w+|#\w+)"
tweets.append('some of @my_story placed and some #tag')
# Use the pattern on the last tweet in the tweets list
mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
print(mentions_hashtags)

# Import the necessary modules
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer
# Use the TweetTokenizer to tokenize all tweets into one list
tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)

german_text='Wann gehen wir Pizza essen? 🍕 Und fährst du mit Über? 🚕'
# Tokenize and print all words in german_text
all_words = word_tokenize(german_text)
print(all_words)

# # Tokenize and print only capital words
capital_words = r"[A-Z\Ü]\w+"
print(regexp_tokenize(german_text, capital_words))

# Tokenize and print only emoji
emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
print(regexp_tokenize(german_text, emoji))

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
# Split the script into lines: lines
# Split the script into lines: lines
lines = holy_grail.split('\n')
print(lines)
# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]
print(lines)
# Tokenize each line: tokenized_lines
pattern_words = "\w+"
tokenized_lines = [regexp_tokenize(s,pattern_words) for s in lines]

# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]
import matplotlib.pyplot as plt
# Plot a histogram of the line lengths
plt.hist(line_num_words)

# Show the plot
plt.show()


# Import Counter
from collections import Counter

# Tokenize the article: tokens
tokens = word_tokenize(holy_grail)
print(tokens)
# Convert the tokens into lowercase: lower_tokens
lower_tokens = [t.lower() for t in tokens]

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)

# Print the 10 most common tokens
print(bow_simple.most_common())


# Import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
# Retain alphabetic words: alpha_only
alpha_only = [t.lower() for t in lower_tokens if t.isalpha()]
print(alpha_only)
# Remove all stop words: no_stops
#nltk.download('stopwords')
stoplist = stopwords.words('english')
no_stops = [t for t in alpha_only if t not in stoplist]
print(no_stops)
#nltk.download('wordnet')
# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
# Lemmatize all tokens into a new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

# Create the bag-of-words: bow
bow = Counter(lemmatized)

# Print the 10 most common tokens
print(bow.most_common(10))

