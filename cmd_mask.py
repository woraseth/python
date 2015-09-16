# used with add.py

from tkinter import *

def button_click():
  import subprocess
  proc = subprocess.run(['python', 'add.py', e0.get(), e1.get()], stdout=subprocess.PIPE)
  label.set(proc.stdout.strip())
  
window = Tk()

e0 = Entry(window)
e0.insert(END, '3')
e0.pack()
e1 = Entry(window)
e1.insert(END, '5')
e1.pack()

label = StringVar()
Label(window, textvariable=label).pack()

Button(window, text="Calculate", command=button_click).pack()

window.mainloop()
