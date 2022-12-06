
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from textblob import TextBlob
import arabic_reshaper
import bidi.algorithm
import time
import webbrowser
import nltk
import camel_tools
from camel_tools.disambig.mle import MLEDisambiguator
import flair
from flair.models import SequenceTagger
from flair.data import Sentence
import re
from collections import deque
from camel_tools.utils.dediac import dediac_ar
"""
reshaped_text= arabic_reshaper.reshape('بسم الله الرحمن الرحيم، الحمد لله رب العالمين ، الرحمن الرحيم، مالك يوم الدين ، ')
bidi_text=bidi.algorithm.get_display(reshaped_text)
bidi_text1=TextBlob(bidi_text)
"""
class Tokenizer:
    def __init__(self, input):
        self.start = 0
        self.current = 0
        self.input = input
        self.tokens = []

    def consume(self):
        self.current += 1
        return self.cur_char()

    def get(self, idx):
        if idx >= len(self.input):
            return None
        return self.input[idx]

    # note: can return None
    def peek(self, amount):
        return self.get(self.current + amount)

    def pop(self):
        self.tokens.append(self.input[self.start:self.current])
        self.start = self.current

    def skip(self):
        self.consume()
        self.start = self.current

    def cur_char(self):
        return self.get(self.current)

    def at_end(self):
        return self.current >= len(self.input)

    def tokenize(self):
        while True:
            # whitespaces and newlines
            cur = self.cur_char()
            if cur is None:
                break
            if re.match('\s', cur) is not None:
                self.skip()
            # words
            elif cur.isalpha():
                self.consume()
                while True:
                    cur = self.cur_char()
                    if cur is None:
                        break
                    if not cur.isalpha():
                        break
                    self.consume()
                self.pop()
            # numbers and floats
            elif cur.isdigit():
                self.consume()
                while True:
                    cur = self.cur_char()
                    if cur is None:
                        break
                    if not cur.isdigit():
                        break
                    self.consume()
                if cur == '.':
                    next = self.peek(1)
                    if next is not None and next.isdigit():
                        cur = self.consume()  # '.'
                        self.consume()  # consider omitting it
                        while True:
                            cur = self.cur_char()
                            if cur is None:
                                break
                            if not cur.isdigit():
                                break
                            self.consume()
                self.pop()
            # floats starting with '.'
            elif cur == '.':
                cur = self.consume()
                if cur is None:
                    pass
                elif cur.isdigit():
                    while True:
                        cur = self.cur_char()
                        if cur is None:
                            break
                        if not cur.isdigit():
                            break
                        self.consume()
                self.pop()
                # punctuation marks
            else:
                self.consume()
                self.pop()
        return self.tokens
    
#source= (Tokenizer("10.5 hibhrllo بسم الله الرحمن الرحيم، الحمد لله رب العالمين").tokenize())
def pre_processing():
    
    source="10.5 hibhrllo بسم الله الرحمن الرحيم، الحمد لله رب العالمين"
    if source != 0:
        t_sentence= source.split(r'،')
        for sent1 in t_sentence:
            Sentence1=Tokenizer(sent1).tokenize()
            for words_sentence in Sentence1:
                print(words_sentence) 
                file_dic= open('file_data.txt','r', encoding="utf-8")# create file
                #file_dic.write(x) # write in file
                file_dic.close() # close file 
                print(file_dic) 
                #text_matching=re.match(file_dic, words_setence)                       
    else:
        print("plase: input text")            
          
pre_processing()

#------ processing -----------
# features----------------
"""x=StringVar()
file_dic= open('file_data.txt','w')# create file
#file_dic.write(x) # write in file
file_dic.close() # close file 
print(file_dic) 
text_matching=re.match(pattern, words_setence)"""  