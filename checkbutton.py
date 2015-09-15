import tkinter as tk
import tkinter.messagebox as tkm

def button_click():
  if chk_var.get() == 0:
    tkm.showinfo("Title", entry.get())
  else:
    tkm.showinfo("Title", float(entry.get()) * 0.9)

window = tk.Tk()

entry = tk.Entry(window)
entry.pack()

chk_var = tk.IntVar()
chk = tk.Checkbutton(window, variable=chk_var, text="Discount")
chk.pack()

button = tk.Button(window, text="Click Me", command=button_click)
button.pack()

window.mainloop()
