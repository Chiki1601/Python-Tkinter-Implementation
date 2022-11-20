#english to hindi translator
# import modules

from tkinter import *
from englisttohindi.englisttohindi import EngtoHindi

# user define function
def eng_to_hindi():
	trans = EngtoHindi(str(e.get()))
	res = trans.convert
	result.set(res)

# object of tkinter
# and background set for grey
master = Tk()
master.configure(bg = 'light grey')

# Variable Classes in tkinter
result = StringVar();

# Creating label for each information
# name using widget Label
Label(master, text="Enter Text : " , bg = "light grey").grid(row = 0, sticky = W)
Label(master, text="Result :", bg = "light grey").grid(row = 3, sticky = W)

# Creating lebel for class variable
# name using widget Entry
Label(master, text="", textvariable=result,bg = "light grey").grid(row = 3,
																column = 1,
																sticky = W)

e = Entry(master, width = 100)
e.grid(row = 0, column = 1)

# creating a button using the widget
# Button that will call the submit function
b = Button(master, text = "Show", command = eng_to_hindi, bg = "Blue")
b.grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5,)

mainloop()
