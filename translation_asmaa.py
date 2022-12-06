import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tokenizer 

from tokenizer import tokenize
from textblob import TextBlob
import arabic_reshaper
import bidi.algorithm
import time
import webbrowser
import nltk
#from rewspaper import Article

#-----create window---
window=tk.Tk()
window.title('Al_Bailey Translator ')
window.geometry('1400x650')
window.config(bg='white')
window.resizable(False,False)
#create variables-----
search_var= StringVar()
#-----create frame---
frame1=Frame(window,width=1370,height=60,bg='whitesmoke')
frame1.pack(pady=8)
frame2=Frame(window,width=1370,height=330,bg='#D1D5DB')
frame2.pack(pady=25)
#-----create label---
Lab1=Label(frame1 ,text='جامعة دمياط',bg='whitesmoke',font=('Arial Bold',12))
Lab1.place(x=1290,y=3)
lab2=Label(frame1 ,text='كلية التربية النوعية ',bg='whitesmoke',font=('Arial Bold',12))
lab2.place(x=1252,y=23)
lab3=Label(frame1,text=' البيلي للترجمة الفورية ', bg='whitesmoke', fg='#1F2937',font=('Arial Bold', 25))
lab3.place(x=570,y=15)
search_var=StringVar()
       
#-----create time & date---
mytime=time.localtime()
mytime1=time.strftime("%d/%m/%Y %H:%M:%S",mytime)
label11=tk.Label(text=mytime1 ,bg='black',fg='gold',font=('Arial Bold',10))
label11.place(x=23,y=72)
#-----create buttons---

#-----create photo---
photo=PhotoImage(file="logo.png")
image1=Label(frame1 ,image=photo)
image1.place(x=10,y=5)
photo1=PhotoImage(file="photo.png")
image2=Label(frame2 ,image=photo1)
image2.place(x=400,y=20)

#-----create functions---
def show1():
    messagebox.showinfo('حول البرنامج','مرحباً بكم : هذا البرنامج يستخدم في الترجمة الفورية من اللغة العربية إلى اللغة الإنجليزية')
    
def s_translat():             
    #-----create window---
    root = Tk()   
    #root = root
    root.geometry('1000x700')
    root.title('Al_Bailey Translator ')
    root.configure(background="silver")
    root.resizable(False,False)
        
             # variables ---------------------
    source_var=StringVar()
    target_var=StringVar()
            #-----create frame & label---------------------    
    frame1=Frame(root,width=1000,height=60,bg='whitesmoke')
    frame1.pack(pady=8)
    lab3=Label(frame1,text=' الترجمة المتخصصة في مجال الحاسوب ', bg='whitesmoke', fg='#1F2937',font=('Arial Bold',20))
    lab3.place(x=300,y=15)
        
            #-----create time & date---
    mytime=time.localtime()
    mytime1=time.strftime("%d/%m/%Y %H:%M:%S",mytime)
    label11=Label(frame1, text=mytime1 ,bg='black',fg='gold',font=('Arial Bold',12))
    label11.place(x=20,y=15)
            #-----create tools--------
    def transletor():
        label5=Label(root,text='تمت الترجمة بنجاح ',bg='whitesmoke',fg='black',font=('Arial Bold',15))
        label5.place(x=430,y=260)
        
    label2=Label(root,text='أدخل النص العربي المُراد ترجمته',bg='silver',fg='black',font=('Arial Bold',15))
    label2.place(x=700,y=80)
    text1=Text(root ,height=17, width=47 )
    text1.place(x=550,y=130)
    label4=Label(root,text='النص مترجم',bg='silver',fg='black',font=('Arial Bold',15))
    label4.place(x=350,y=80)
    text2=Text(root, height=17, width=47)
    text2.place(x=60,y=130)

    Button14=Button(root,text='ترجم',width=5, bg='#60A5FA',fg='#333',font=('Arial Bold',15,'bold'),cursor="hand2")
    Button14.place(x=460,y=230)
            
    label4=Label(root,text='ترجمة عامة',bg='silver',fg='black',font=('Arial Bold',15))
    label4.place(x= 850,y=530)
    combo_search=ttk.Combobox(root,values=('Google Translate','Microsoft Bing','Reverso'),state='readonly')
    combo_search.current(0)
    #--- create function for General translation -----------
    def G_translat():
        site=StringVar()
        site=combo_search.get()   
        if site == 'Google Translate':
            webbrowser.open('https://translate.google.com.eg/')
        elif site== 'Microsoft Bing':    
            webbrowser.open('https://www.bing.com/translator')
        else:
             webbrowser.open('https://www.reverso.net/traduction-texte')    
    combo_search.place(x=800,y=570)
    
    # --- create buttons ---------------------
    Button6=Button(root,text='ترجم',bg='#60A5FA',fg='#333',width=5 ,font=('Arial Bold',15,'bold'),cursor="hand2",command=G_translat)
    Button6.place(x=700,y=570)          
    Button7=Button(root,text=' غلق البرنامج  ',bg='#60A5FA',fg='#333',width=9 ,font=('Arial Bold',15,'bold'),cursor="hand2",command=window.quit)
    Button7.place(x=50,y=570 )
        
    root.mainloop()
        
                #   ------------الخوارزمية------------------

                    #---1- pre_processing ------------------------------------

#---create buttons -----------   
label4=Label(window,text='اختيار نوع الترجمة ',font=('Arial Bold',16), bg='#D1D5DB')
label4.place(x=1200,y=140)
label4=Label(window,text='ترجمة عامة',font=('Arial Bold',15),width=9 ,bg='#60A5FA',fg='#333',border=5)
label4.place(x=1230,y=180)
#---create combobox for translation ------------
combo_search=ttk.Combobox(window,values=('Google Translate','Microsoft Bing','Reverso'),state='readonly')
combo_search.current(0)

#--- create function for General translation -----------
def G_translat():
    site=StringVar()
    site=combo_search.get()   
    if site == 'Google Translate':
        webbrowser.open('https://translate.google.com.eg/')
    elif site== 'Microsoft Bing':    
        webbrowser.open('https://www.bing.com/translator')
    else:
        webbrowser.open('https://www.reverso.net/traduction-texte')
        
combo_search.place(x=1070,y=180)
    
Button6=Button(window,text='ترجم',bg='#60A5FA',fg='#333',width=5 ,font=('Arial Bold',13,'bold'),cursor="hand2",command=G_translat)
Button6.place(x=1000,y=180)
Button9=Button(window,text='ترجمة متخصصة',bg='#60A5FA',fg='#333',width=9 ,font=('Arial Bold',15,'bold'),cursor="hand2",command=s_translat)
Button9.place(x=1230,y=260)            
 
Button6=Button(window,text='حول البرنامج',bg='#60A5FA',fg='#333',width=9 ,font=('Arial Bold',15,'bold'),cursor="hand2",command=show1)
Button6.place(x=50,y=180)
Button7=Button(window,text=' غلق البرنامج  ',bg='#60A5FA',fg='#333',width=9 ,font=('Arial Bold',15,'bold'),cursor="hand2",command=window.quit)
Button7.place(x=50,y=260 )

window.mainloop()


