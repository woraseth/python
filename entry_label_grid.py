import tkinter as tk
import tkinter.messagebox as tkm

def hello():
   tkm.showinfo("Title", entry.get())

window = tk.Tk()

#-------------------------------
label = tk.Label(window, text='Name')
label.grid(row=0, column=0)

entry = tk.Entry(window)
entry.grid(row=0, column=1)
#-------------------------------
button = tk.Button(window, text="Click Me", command=hello)
button.grid(row=1, column=0, columnspan=2)

window.mainloop()
