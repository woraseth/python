import tkinter as tk
import tkinter.messagebox as tkm

def hello():
   tkm.showinfo("Title", entry.get())

window = tk.Tk()

#-------------------------------
frame = tk.Frame(window)
frame.pack()

label = tk.Label(frame, text='Name')
label.pack(side=tk.LEFT)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)
#-------------------------------
button = tk.Button(window, text="Click Me", command=hello)
button.pack()

window.mainloop()
