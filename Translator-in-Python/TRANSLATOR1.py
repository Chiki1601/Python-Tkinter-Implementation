# Translator in python

from translate import Translator
from tkinter import *
win=Tk()
win.title("Translator")
win.geometry('290x220')
win.configure(bg='light cyan')

def French():
    word = E1.get()
    translator=Translator(to_lang='French')
    translation = translator.translate(word)
    l2=Label(win,text=f'translated word : {translation}',font=('Arial Bold',12),fg='DodgerBlue2')
    l2.place(x=5, y=180)

def german():
    word = E1.get()
    translator = Translator(to_lang='German')
    translation = translator.translate(word)
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial  Bold', 12), fg='DodgerBlue2')
    l2.place(x=5,y=180)
def spanish():
    word = E1.get()
    translator = Translator(to_lang='Spanish')
    translation = translator.translate(word)
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
    l2.place(x=5,y=180)
def hindi():
    word = E1.get()
    translator = Translator(to_lang='Hindi')
    translation = translator.translate(word)
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
    l2.place(x=5,y=180)
def turkish():
    word = E1.get()
    translator = Translator(to_lang='Turkish')
    translation = translator.translate(word)
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
    l2.place(x=5, y=180)
def chinese():
    word = E1.get()
    translator = Translator(to_lang='Chinese')
    translation = translator.translate(word)
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
    l2.place(x=5, y=180)
def Arabic():
    word = E1.get()
    translator = Translator(to_lang='Arabic')
    translation = translator.translate(word)
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
    l2.place(x=5, y=180)
def Persian():
    word = E1.get()
    translator = Translator(to_lang='Arabic')
    translation = translator.translate(word)
    word= " "
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
    l2.place(x=5,y=180)

txt=StringVar()
l1=Label(win,text="Enter your text Here!!")
l1.place(x=40,y=3)
l3=Label(win,text="Translation:",font=('Bold',10))
l3.place(x=5,y=160)
E1=Entry(win,textvariable=txt,width=23,font=('Arial Bold',15),bg="white")
E1.place(x=17,y=20)
Btn1=Button(win,text='French',padx=8,pady=8,bg="powder blue",width=6,command=French)
Btn1.place(x=5,y=55)
Btn2=Button(win,text='German',padx=8,pady=8,bg="yellow",width=6,command=german)
Btn2.place(x=75,y=55)
Btn3=Button(win,text='Spanish',padx=8,pady=8,bg="blue",width=6,command=spanish)
Btn3.place(x=145,y=55)
Btn4=Button(win,text='Hindi',padx=8,pady=8,bg="Green",width=6,command=hindi)
Btn4.place(x=215,y=55)
Btn5=Button(win,text='Turkish',padx=8,pady=8,bg="Pink",width=6,command=turkish)
Btn5.place(x=5,y=100)
Btn6=Button(win,text='Chinese',padx=8,pady=8,bg="orange",width=6,command=chinese)
Btn6.place(x=75,y=100)
Btn7=Button(win,text='Arabic',padx=8,pady=8,bg="white",width=6,command=Arabic)
Btn7.place(x=145,y=100)
Btn8=Button(win,text='Persian',padx=8,pady=8,bg="DodgerBlue2",width=6,command=Persian)
Btn8.place(x=215,y=100)
win.mainloop()
