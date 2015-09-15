import tkinter as tk
import tkinter.messagebox as tkm

def button_click():
  tkm.showinfo("Title", entry.get())

window = tk.Tk()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Click Me", command=button_click)
button.pack()

window.mainloop()

