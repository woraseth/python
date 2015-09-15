import tkinter as tk
import tkinter.messagebox as tkm

def button_click():
  tkm.showinfo("Title", spn.get())

window = tk.Tk()

spn = tk.Spinbox(window, values=('Mr', 'Miss', 'Mrs'))
spn.pack()

tk.Button(window, text="Click Me", command=button_click).pack()

window.mainloop()
