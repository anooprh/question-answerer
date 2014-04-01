import nltk
import re

fo = open('story.txt', 'r')
text = fo.read()
text = re.sub('\n', ' ', text)
sentences = nltk.sent_tokenize(text)
questions = filter(lambda x: '?' in x, sentences)

print questions



