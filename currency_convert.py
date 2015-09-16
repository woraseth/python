from tkinter import *
from tkinter.messagebox import *

def enter_pressed(event):
  thb = float(txt_usd.get()) * 30
  thb_var.set(thb)
  
window = Tk()

txt_usd = Entry(window)
txt_usd.pack()
txt_usd.bind('<Return>', enter_pressed)

thb_var = StringVar()
Label(window, textvariable=thb_var).pack(anchor=W)

window.mainloop()
