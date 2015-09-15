import tkinter as tk
import tkinter.messagebox as tkm

def button_click():
  if rdo_var.get() == 0:
    tkm.showinfo("Title", entry.get())
  elif rdo_var.get() == 1:
    tkm.showinfo("Title", float(entry.get()) * 0.9)
  else:
    tkm.showinfo("Title", float(entry.get()) * 0.8)

window = tk.Tk()

entry = tk.Entry(window)
entry.pack()

rdo_var = tk.IntVar()
tk.Radiobutton(window, text="0%",  variable=rdo_var, value=0).pack()
tk.Radiobutton(window, text="10%", variable=rdo_var, value=1).pack()
tk.Radiobutton(window, text="20%", variable=rdo_var, value=2).pack()

tk.Button(window, text="Click Me", command=button_click).pack()

window.mainloop()
