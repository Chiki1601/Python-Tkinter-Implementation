#importing necessary packages
from tkinter import *
import random, string

#Root window
root = Tk()
root.geometry("400x280")
root.title("Password Generator")

title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("Select the strength of the password:")


def selection():
    global selection
    selection = choice.get()


#Selecting password strength
choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root, text="STRONG", variable=choice, value=3, command=selection).pack(anchor=CENTER)
labelchoice = Label(root)
labelchoice.pack()

#Selecting Password length
lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel).pack()

#Length selection
val = IntVar()
spinlenght = Spinbox(root, from_=4, to_=24, textvariable=val, width=13).pack()

# passprint


def callback():
    lsum.config(text=passgen())


# clickable button
passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3, bg='lightblue')
passgenButton.pack()
password = str(callback)

# password result message
lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

# function
poor= string.ascii_uppercase + string.ascii_lowercase
average= string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor+ average + symbols

#Generate random password of specified length
def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))


root.mainloop()
