import tkinter as tk
root = tk.Tk()
v = tk.IntVar()
v.set(1)
languages=[("Python",1), ("JS",2), ("C++",3), ("C",4)]

def ShowChoice():
    print(v.get())

tk.Label(root, text="""Choose a programming language""",
         justify = tk.LEFT, padx = 20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root, text=language, padx=20, variable=v, command=ShowChoice, value=val).pack(anchor=tk.W)

root.mainloop()
