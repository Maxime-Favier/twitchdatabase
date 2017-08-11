from tkinter import *


def getname():
    global pseudo
    pseudo = name.get()
    window.destroy()
    # print(pseudo)


window = Tk()
pseudo = ""
name = StringVar()


tutorial = Label(window, text="twitch username:", font=("Helvetica", 12))
name = Entry(window, textvariable=name, width=20)
line_break = Label(window, text= " ", font=("Helvetica", 16))
stop = Button(text="quit", command=quit, font=("Helvetica", 10))
ok = Button(text="Ok", command=getname, font=("Helvetica", 16))

tutorial.grid(row=0, column=1)
name.grid(row=0, column=2, columnspan=2)
line_break.grid(row=2)
stop.grid(row=3, column=1)
ok.grid(row=3, column=3)


window.mainloop()
print(pseudo)


