import nltk
import re

fo = open('story.txt', 'r')
text = fo.read()
text = re.sub('\n', ' ', text)
sentences = nltk.sent_tokenize(text)
questions = filter(lambda x: '?' in x, sentences)

print questions

my_questions = ['What is your favourite drink?', 'Where am I?', 'What is the temperature?', 'How old are you?']
formatted_questions = []

for question in my_questions:
    q_tokenized = nltk.word_tokenize(question)
    q_tagged = nltk.pos_tag(q_tokenized)
    formatted_questions.append(q_tagged)

for question in formatted_questions:
    print question
