import tkinter as tk
root = tk.Tk()
logo = tk.PhotoImage(file="shah-logo.png")
w1 = tk.Label(root, image=logo).pack(side="right")
explanation = """Some text with logo using tkinter GUI """
w2 = tk.Label(root, justify=tk.LEFT, padx=10, text=explanation).pack(side="left")
root.mainloop()
