from requests import get
import re
import xlwt
from xlwt import Workbook
# create DB in EXCEL
wb=Workbook()
sheet1=wb.add_sheet('sheet1')
sheet1.write(0,0,'id')
sheet1.write(0,1,'name')
wb.save('EX.xls')
"""for x in wb:
    print(x)"""
    # انشاء ملف  نصي والكتابة فيه
f= open("dic1.txt",encoding="utf-8")
print(f.read())
f.close()
        #  create file

    
#f.write(x)# write in file
#print(f)

# جلب البيانات وحفظها في متغيرات
#n1=inp1.get()#الاداة  (inp1) - اسم المتغير (n1)

#go=get(أسم متغير).text # احفظ المتغير كنص في المتغير go
bidi_text='''
contact with soso: soso$sdff
contact with asmaa: asmaa@gmail.com'''
res=re.findall('\S+@\S+', bidi_text)# findall دالة للبحث داخل البيانات عن شي معين
for x in res:
    print(x)
    # انشاء ملف  نصي والكتابة فيه
f1= open('dic1.txt','r',encoding="utf-8")# create file
for line in f1.readlines():
    
#f.write(x)# write in file
    print(line)
f1.close() # close file   

#sent=re.split('\.+\؟\+:\+،\+؛',bidi_text1) 
#print(res)
#bidi_text1.split(r'،')

"""for sent1 in t_sentence:
    
    sentence=sent1.split(' ')
            #sentence= sentence
    for words_sentence in sentence:
        print(words_sentence)
    else:
        print("plase: input text")  
def is_allowed(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)
string='بسم الله الرحمن الرحيم'
print(is_allowed("ABCDEFabcdef123450")) 
print(is_allowed("*&%@#!}{"))
"""
