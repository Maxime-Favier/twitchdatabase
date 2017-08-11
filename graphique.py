from tkinter import *


def getname():
    print("yop")

window = Tk()

name = StringVar()
pseudo = ''

tutorial = Label(window, text="twitch username")
name = Entry(window, textvariable=name, width=50)
stop = Button(text="quit", command=quit).grid(row=2, column=0)
ok = Button(text="Ok", command=getname()).grid(row=2, column=1)

tutorial.grid(row=0, column=0)
name.grid(row=0, column=0)


window.mainloop()
