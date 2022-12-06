
import nltk
import re
from tokenizer import tokenize
from textblob import TextBlob
from textblob import Word
import arabic_reshaper
from bidi.algorithm import get_display

x=str()
text=(".أحب البيزا . إنها رائعة في الشتاء")
x=arabic_reshaper.reshape(text)
x1=get_display(x)

text_blob_object=TextBlob(x1)
print(text_blob_object.sentences)
print()
for word, pos in text_blob_object.tags:
    print((word + "=>" )+ pos)
#print(text_blob_object_arabic.translate(to="en"))
