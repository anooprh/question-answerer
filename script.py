import nltk
import re

fo = open('story.txt', 'r')
text = fo.read()
text = re.sub('\n', ' ', text)
sentences = nltk.sent_tokenize(text)
questions = filter(lambda x: '?' in x, sentences)

print questions

my_questions = ['What is your favourite drink?', 'Where am I?', 'What is the temperature?', 'How old are you?']
formatted_questions = [];

for question in my_questions:
    sentences = nltk.sent_tokenize(question)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences];
    formatted_questions.append(sentences)

for question in formatted_questions:

pass
