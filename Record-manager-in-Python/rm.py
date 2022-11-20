from tkinter import*
import tkinter.messagebox as tmsg



root = Tk()

root.geometry("900x500")
root.minsize(900,500)
root.maxsize(900,500)
root.title("Record Manager")


#creating functions

def submit():
    with open("record.txt", "a") as f:
        f.write(f"Username = {nameValue.get()}, Password = {passValue.get()}, Email = {emailValue.get()}, Phone number = {phoneValue.get()}, agreement = {agreementValue.get()}\n")

def new():
    pass

def help():
    tmsg.showinfo("Help", "This application is developed by Dev!")

def save():
    pass

def saveas():
    pass

def exit():
    a = tmsg.askquestion("Exit?", "Are you sure sir?")
    if a=="yes":
        b = tmsg.askquestion("Again!", "Think again sir!")
        if b=="yes":
           c = tmsg.askquestion("Again!", "Please, think again sir!")
        if c=="yes":
               d = tmsg.askquestion("Again!", "No, think again and again sir!!!!")
        if d=="yes":
                    tmsg.askquestion("Finally", "Ok OK, you win!")
                    root.destroy()
def feedback():
    l = tmsg.askquestion("Experience", "Was your experience good?")
    
    if l=="yes":
                tmsg.showinfo("Yes!", "Good, now go to our official website to rate us!")
    else:
                tmsg.showinfo("No!", "Get Lost!")

                
def update():
    msg = tmsg.askretrycancel("Sorry!", "Server is busy, so update is not available")
    if msg:
        tmsg.showinfo("Sorry", "I already told you, update is not availble, get lost! ")
    else:
        tmsg.showinfo("Good", "You are a good person, try later!")


def readme():
    tmsg.showinfo("ReadMe", "You can see the record in records.txt file in same directory of this application.")


# def size():
#     size = Tk()
#     size.geometry("400x300")
#     size.title("Set your wizard size")
    
#     def sized():
#         width = widthValue.get()
#         height = heightValue.get()
        
#         root.geometry(f"{width}x{height}")
        
#         tmsg.showinfo("Size set", "Size is successfully set, according to your choice!")
#         root.destroy()
    
#     a = Label(size, text="width")
#     b = Label(size, text="height")
    
#     a.grid(row=2, column=3)
#     b.grid(row=3, column=3)
    
#     widthValue = StringVar()
#     heightValue = StringVar()
    
#     Entry(size, textvariable=widthValue).grid(row=2, column=4)
#     Entry(size, textvariable=heightValue).grid(row=3, column=4)
    
#     Button(size, text="Set Size", command=sized).grid(row=4, column=4)

def color():
    pass

def happy():
    root = Tk()
    root.geometry("400x100")
    root.minsize(400,100)
    root.maxsize(400,100)
    root.title("Please rate us!")
    
    def rate():
        
        tmsg.showinfo("Done", f"Thank You, for rating us {Rate.get()}!")
        
        with open("rate.txt", "a") as f:
            f.write(f"Person rated = {Rate.get()}\n")

        root.destroy()
              
    Rate = Scale(root, from_=0, to=50, tickinterval=10, orient=HORIZONTAL)
    Rate.pack()
    
    b0 = Button(root, text="Rate", bg="yellow", command=rate)
    b0.pack()


#labelling the main components
Label (root, text="Kindly fill the following details:-", font="lucida 20 bold", pady=30, bg="yellow" ).grid(row=0, column=4)

Label(root, text="First name\t \t -", font="lucida 15 bold", padx=10).grid(row=1, column=3)
Label(root, text="Surname name\t \t -", font="lucida 15 bold", padx=10).grid(row=2, column=3)
Label(root, text="Password\t \t -", font="lucida 15 bold").grid(row=3, column=3)
Label(root, text="E-mail address\t \t -", font="lucida 15 bold", padx=10).grid(row=4, column=3)
Label(root, text="Phone number\t \t -", font="lucida 15 bold", padx=10).grid(row=5, column=3)


#creating some variable values

nameValue = StringVar()
surnameValue = StringVar()
passValue = StringVar()
emailValue = StringVar()
phoneValue = StringVar()
agreementValue = IntVar()

#checkbutton

agreement = Checkbutton(text="Have you read our agreement?", variable=agreementValue)
agreement.grid(row=6, column=4)

#creating entry widgets

Entry(root, textvariable=nameValue).grid(row=1, column=4)
Entry(root, textvariable=surnameValue).grid(row=2, column=4)
Entry(root, textvariable=passValue).grid(row=3, column=4)
Entry(root, textvariable=emailValue).grid(row=4, column=4)
Entry(root, textvariable=phoneValue).grid(row=5, column=4)



#creating buttons for submission data

Button(root, text="Submit", command=submit).grid(row=7, column=4)

#creating menu

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command (label="New", command=new)
m1.add_command(label="Save", command=save)
m1.add_command (label="Save as", command=saveas)
m1.add_separator()
m1.add_command (label="Exit", command=exit)

mainmenu.add_cascade(label="File", menu=m1)
root.config(menu=mainmenu)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command (label="Help", command=help)
m2.add_command (label="Feedback", command=feedback)
m2.add_command (label="Update", command=update)
m2.add_command (label="See ReadMe", command=readme)
m2.add_command (label="Rate", command=happy)
mainmenu.add_cascade(label="More", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
# m3.add_command(label="Set Wizard Size", command=size)
m3.add_command(label="Set Wizard's Colour", command=color)
mainmenu.add_cascade(label="View", menu=m3)



root.mainloop()
