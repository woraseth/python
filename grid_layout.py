from tkinter import *

window = Tk()

#--------------------------------------------
label0 = Label(window, text='Name')
label0.grid(row=0, column=0, sticky=W)

entry0 = Entry(window)
entry0.grid(row=0, column=1)
#--------------------------------------------
label1 = Label(window, text='Family Name')
label1.grid(row=1, column=0)

entry1 = Entry(window)
entry1.grid(row=1, column=1)
#--------------------------------------------
button = Button(window, text="OK")
button.grid(row=2, column=0, columnspan=2, sticky=W+E, padx=5, pady=5)
#--------------------------------------------

window.mainloop()
