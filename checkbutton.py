from tkinter import *
from tkinter.messagebox import *

def button_click():
  if chk_var.get() == 0:
    price = entry.get()
  else:
    price = float(entry.get()) * 0.9
  showinfo('Title', price)

window = Tk()

entry = Entry(window)
entry.pack()

chk_var = IntVar()
Checkbutton(window, variable=chk_var, text='Discount').pack()

Button(window, text='Calculate', command=button_click).pack()

window.mainloop()
