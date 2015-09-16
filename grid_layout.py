from tkinter import *

window = Tk()

#--------------------------------------------
label = Label(window, text='Name')
label.grid(row=0, column=0, sticky=W)

entry = Entry(window)
entry.grid(row=0, column=1)
#--------------------------------------------
label = Label(window, text='Family Name')
label.grid(row=1, column=0)

entry = Entry(window)
entry.grid(row=1, column=1)
#--------------------------------------------
button = Button(window, text="OK")
button.grid(row=2, column=0, columnspan=2, sticky=W+E, padx=5, pady=5)
#--------------------------------------------

window.mainloop()
