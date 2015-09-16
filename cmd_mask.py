from tkinter import *

def button_click():
  import subprocess
  args = ['python', 'add.py', entry0.get(), entry1.get()]
  proc = subprocess.run(args, stdout=subprocess.PIPE)
  label.set(proc.stdout.strip())
  
window = Tk()

entry0 = Entry(window)
entry0.pack()
entry1 = Entry(window)
entry1.pack()

label = StringVar()
Label(window, textvariable=label).pack()

Button(window, text="Calculate", command=button_click).pack()

window.mainloop()
