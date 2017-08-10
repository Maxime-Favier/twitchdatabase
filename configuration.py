from tkinter import *


class Interface(Frame):

    def __init__(self, window, **kwargs):

        Frame.__init__(self, window, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.name = StringVar()
        self.var = ''

        # widget creation
        self.tutorial = Label(window, text="please type your twitch username")
        self.name = Entry(window, textvariable=self.name, width=50)
        self.quit = Button(self, text="quit", command=self.quit)
        self.ok = Button(self, text="Ok", command=self.getname)

        # widget display
        self.tutorial.pack(side="top")
        self.name.pack(side="top")
        self.quit.pack(side="left")
        self.ok.pack(side="right")

    def getname(self):

        self.var = self.name.get()
        print(self.var)

twitchdatabase = Tk()
interface = Interface(twitchdatabase)
interface.mainloop()
interface.destroy()
