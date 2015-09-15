import tkinter as tk
import tkinter.messagebox as tkm

class MyFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        tkm.showinfo("Title", "Hello World")

root = tk.Tk()

app = MyFrame(master=root)
app.mainloop()
