import spacy
from spacy import displacy
from collections import Counter
import talon 


nlp = spacy.load("en_core_web_sm")

doc = nlp('European authorities fined L. Müller a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
print([(X.text, X.label_) for X in doc.ents])