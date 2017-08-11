from tkinter import *


class Interface(Frame):

    def __init__(self, window, **kwargs):

        Frame.__init__(self, window, width=768, height=576, **kwargs)
        # self.pack(fill=BOTH)
        self.name = StringVar()
        self.var = ''

        # widget creation
        self.tutorial = Label(window, text="please type your twitch username").grid(row=0)
        self.name = Entry(window, textvariable=self.name, width=50).grid(row=1)
        self.quit = Button(self, text="quit", command=self.quit).grid(row=2)
        self.ok = Button(self, text="Ok", command=self.getname).grid(row=3)

        # grid settings
        #self.tutorial.grid(row=0)
        #self.name.grid(row=1)
        #self.quit.grid(row=2)
        #self.ok.grid(row=3)
        print("get2")

        # widget display
        #self.tutorial.pack()
        #self.name.pack()
        #self.quit.pack()
        #self.ok.pack()

    def getname(self):

        self.var = self.name.get()
        print(self.var)

twitchdatabase = Tk()
interface = Interface(twitchdatabase)
interface.mainloop()
interface.destroy()
