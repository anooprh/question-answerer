import nltk

fo = open('story.txt', 'r')
text = fo.read()
sentences = nltk.sent_tokenize(text)

