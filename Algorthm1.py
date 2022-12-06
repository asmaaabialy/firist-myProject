
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from textblob import TextBlob
from textblob import Word
import time
import webbrowser
import nltk 
import re
import googletrans
from googletrans import Translator
import tokenizer
from tokenizer import Tokenizer

#translator = Translator()
#print(translator.translate('مرحبا').text)
#print("Sourc Language:" + translator.src)
"""
"""
class translat:
          
    #-----create window---
    def __init__(self, root):
        root = root
        root.geometry('1000x700')
        root.title('برنامج للترجمة المُتخصصة في مجال الحاسوب')
        root.configure(background="silver")
        root.resizable(False,False)
        
    # variables ---------------------
        self.source_var=StringVar()
        self.target_var=StringVar()
    #-----create frame & label---------------------    
        frame1=Frame(root,width=1000,height=60,bg='whitesmoke')
        frame1.pack(pady=8)
        lab3=Label(frame1,text=' البيلي للترجمة الفورية ', bg='whitesmoke', fg='#1F2937',font=('Arial Bold',23))
        lab3.place(x=370,y=15)
        
    #-----create time & date---
        mytime=time.localtime()
        mytime1=time.strftime("%d/%m/%Y %H:%M:%S",mytime)
        label11=Label(frame1, text=mytime1 ,bg='black',fg='gold',font=('Arial Bold',12))
        label11.place(x=20,y=15)
    #-----create tools--------
        def transletor():
            #self.source_var=text1.get()
            self.source_var="بسم الله الرحمن الرحيم، الحمد لله رب العالمين ، الرحمن الرحيم"
            text_var=Tokenizer("بسم الله الرحمن الرحيم، الحمد لله رب العالمين ، الرحمن الرحيم").tokenize()
            #text_var1=(r'\،\n',self.source_var)
            label4=Label(root,text=text_var, bg='whitesmoke',fg='black',font=('Arial Bold',15))
            label4.place(x=350,y=420)
            
            label5=Label(root,text='تمت الترجمة بنجاح ',bg='whitesmoke',fg='black',font=('Arial Bold',15))
            label5.place(x=430,y=560)
        
        label2=Label(root,text='أدخل النص العربي المُراد ترجمته',bg='silver',fg='black',font=('Arial Bold',15))
        label2.place(x=700,y=80)
        text1=Text(root ,height=17, width=47 )
        text1.place(x=550,y=130)
        #self.source_var== text1.get()
        """def transletor():
            #n1=text1.get()
            label4=Label(root,text=text1, bg='whitesmoke',fg='black',font=('Arial Bold',15))
            label4.place(x=350,y=420)
            
        """
        label4=Label(root,text='النص مترجم',bg='silver',fg='black',font=('Arial Bold',15))
        label4.place(x=350,y=80)
        text2=Text(root, height=17, width=47)
        text2.place(x=60,y=130)
        Button14=Button(root,text='ترجم',width=5, bg='#60A5FA',fg='#333',font=('Arial Bold',15,'bold'),cursor="hand2", command=transletor)
        Button14.place(x=460,y=230)
        
#   ------------الخوارزمية------------------

#---1- pre_processing ------------------------------------
"""    
        text_var="بسم الله الرحمن الرحيم، الحمد لله رب العالمين ، الرحمن الرحيم"
        label5=Label(root,text="بسم الله الرحمن الرحيم ", bg='whitesmoke',fg='black',font=('Arial Bold',15))
   sent=StringVar()
    t_sentence= bidi_text.split('،')
for sent1 in t_sentence:
    
    for word_s in (sent1):
        w_sentence= simple_word_tokenize(sent1)
        print(w_sentence)
print(bidi_text1.split(u'،')) 
print(bidi_text1.words)
        
"""
        #print(bidi_text1.detect_language()) 
        #text111= TextBlob("i love you") 
        #print(bidi_text1.translate(to = 'ar'))

#label1=Label(root, text=bidi_text,bg='black',fg='gold',font=('Arial Bold',15))
#label1.place(x=100,y=590)        

root = Tk()
ob = translat(root)

root.mainloop()





    


























