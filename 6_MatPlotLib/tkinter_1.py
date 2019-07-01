from tkinter import *
root = Tk()

def stopProg(e):
    root.destroy()

def transfertext(e):
    label1.configure(text="Hello World")

button1=Button(root,text="Exit")
button1.pack()
button1.bind('<Button-1>',stopProg)

button2=Button(root,text="Click me to update Some text")
button2.pack()
button2.bind('<Button-1>',transfertext)

label1=Label(root,text="Some text")
label1.pack()

root.mainloop()
