from tkinter import *
from tkinter.messagebox import *

def button_click():
  showinfo('Title', 'Hello, ' + entry.get())
     
window = Tk()

entry = Entry(window)
entry.pack(padx=10, pady=5)

Button(window, text='Click Me', command=button_click).pack(pady=5)

window.mainloop()
