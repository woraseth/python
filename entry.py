import tkinter as tk
import tkinter.messagebox as tkm

def hello():
  tkm.showinfo("Title", entry.get())

window = tk.Tk()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Click Me", command=hello)
button.pack()

window.mainloop()

