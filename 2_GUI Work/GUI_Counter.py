import tkinter as tk

counter = 0
def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text = str(counter))
        label.after(100,count)
    count()

root = tk.Tk()
root.title("Counting 10th of seconds")
label = tk.Label(root, fg="Red")
label.pack()
counter_label(label)
button = tk.Button(root, text="STOP", width = 25, command = root.destroy)
button.pack()
root.mainloop()
