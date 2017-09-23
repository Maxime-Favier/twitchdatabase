def channelselect(debug=0):

    import tkinter

    # get name function
    def getname():
        global pseudo
        pseudo = name.get()
        window.destroy()

    window = Tk()
    # window title
    window.wm_title("Twitch database - pseudo")

    # variables
    pseudo = ""
    name = StringVar()

    # define labels and buttons
    twitch_database = Label(window, text="TwitchDatabase", font=("Helvetica", 14))
    line_break_1 = Label(window, text=" ", font=("Helvetica", 5))
    tutorial = Label(window, text="twitch username:", font=("Helvetica", 11))
    name = Entry(window, textvariable=name, width=20)
    line_break_2 = Label(window, text=" ", font=("Helvetica", 11))
    stop = Button(text="QUIT", command=quit, font=("Helvetica", 11))
    ok = Button(text="OK", command=getname, font=("Helvetica", 11))
    line_break_3 = Label(window, text=" ", font=("Helvetica", 5))

     # window configuration
    twitch_database.grid(row=1, columnspan=5)
    line_break_1.grid(row=2)
    tutorial.grid(row=3, column=1, sticky=W)
    name.grid(row=3, column=2, columnspan=2, padx=10, sticky=W)
    line_break_2.grid(row=4)
    stop.grid(row=5, column=1)
    ok.grid(row=5, column=3)
    line_break_3.grid(row=6)

    window.mainloop()

    if debug==1:
        print(pseudo)

    return pseudo
