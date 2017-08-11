from tkinter import *


def getname():
    pseudo = name.get()
    print(pseudo)


window = Tk()

name = StringVar()

tutorial = Label(window, text="twitch username")
name = Entry(window, textvariable=name, width=20)
stop = Button(text="quit", command=quit)
ok = Button(text="Ok", command=getname)

tutorial.grid(row=0, column=1)
name.grid(row=0, column=2, columnspan=2)
stop.grid(row=2, column=1)
ok.grid(row=2, column=3)


window.mainloop()
