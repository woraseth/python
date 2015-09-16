import tkinter as tk
import tkinter.messagebox as tkm

def hello():
   tkm.showinfo("Title", "Hello World")

window = tk.Tk()

button = tk.Button(window, text = "Click Me", command=hello)
button.pack()

window.mainloop()

