import tkinter as tk
import tkinter.messagebox as tkm

def hello():
   tkm.showinfo("Title", "Hello World")

top = tk.Tk()

b1 = tk.Button(top, text = "Click Me", command=hello)
b1.pack()

top.mainloop()
