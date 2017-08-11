from tkinter import *


def getname():
    global pseudo
    pseudo = name.get()
    window.destroy()
    # print(pseudo)


window = Tk()
pseudo = ""
name = StringVar()


twitchdatabase = Label(window, text= "TwitchDatabase", font=("Helvetica", 14))
line_break_1 = Label(window, text= " ", font=("Helvetica", 11))
tutorial = Label(window, text="twitch username:", font=("Helvetica", 11))
name = Entry(window, textvariable=name, width=20)
line_break_2 = Label(window, text= " ", font=("Helvetica", 11))
stop = Button(text="quit", command=quit, font=("Helvetica", 11))
ok = Button(text="Ok", command=getname, font=("Helvetica", 11))

twitchdatabase.grid(row=1, columnspan=5)
line_break_1.grid(row=2)
tutorial.grid(row=3, column=1)
name.grid(row=3, column=2, columnspan=2)
line_break_2.grid(row=4)
stop.grid(row=5, column=1)
ok.grid(row=5, column=3)


window.mainloop()
print(pseudo)


