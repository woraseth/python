from tkinter import *

window = Tk()

#--------------------------------------------
label0 = Label(window, text='0,0')
label0.grid(row=0, column=0, sticky=W, padx=20)

entry0 = Entry(window)
entry0.insert(END, '0,1')
entry0.grid(row=0, column=1, padx=20)
#--------------------------------------------
label1 = Label(window, text='1,0')
label1.grid(row=1, column=0, padx=20)

entry1 = Entry(window)
entry1.insert(END, '1,1')
entry1.grid(row=1, column=1, padx=20)
#--------------------------------------------
button = Button(window, text="2,0 span 2 columns")
button.grid(row=2, column=0, columnspan=2, sticky=W+E, padx=5, pady=5)
#--------------------------------------------

window.mainloop()
