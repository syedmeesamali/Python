from tkinter import *
root = Tk()
def stopProg(e):
    root.destroy()
    
button1=Button(root,text="click to close")
button1.pack()
button1.bind('<Button-1>',stopProg)

root.mainloop()
