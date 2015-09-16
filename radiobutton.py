from tkinter import *
from tkinter.messagebox import *

def button_click():
  print(rdo_var.get())
  price = float(entry.get()) * (100-rdo_var.get()) / 100
  showinfo("Title", price)

window = Tk()

entry = Entry(window)
entry.pack()

rdo_var = IntVar()
Radiobutton(window, text="10%", variable=rdo_var, value=10).pack()
Radiobutton(window, text="20%", variable=rdo_var, value=20).pack()
Radiobutton(window, text="25%", variable=rdo_var, value=25).pack()

Button(window, text="Calculate", command=button_click).pack()

window.mainloop()
