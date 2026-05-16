from SimpleTokenizer import SimpleTokenizer
import re
with open("sample.txt","r") as f:
    raw = f.read()

preprocessed = re.split(r'([,.:;? \s])',raw)

preprocessed = [items.strip() for items in preprocessed if items.strip()]

words = sorted(set(preprocessed))## sorted set of non repeating wprds de degea

vocab = {str:id for id,str in enumerate(words) }

tok = SimpleTokenizer(vocab)

text  = raw[:50]

encodings = tok.encode(text)

print(encodings)

