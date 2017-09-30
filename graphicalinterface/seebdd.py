from tkinter import *



window = Tk()
    # window title
window.wm_title("Twitch database - pseudo")

    # variables
name = StringVar()

# define labels and buttons


try:
    import sqlite3  # sql package

except ImportError:
    raise ImportError("unable to find lib: sqlite3 and/or time")

first_run = 0

# check if that is the first run
try:
    config = open("../config/first-run.conf", "r")

except FileNotFoundError:
    print("first run!")
    config = open("../config/first-run.conf", "w")
    config.write("first-run = true")
    first_run = 1

finally:

    # connect to the database
    database_path = "../database/viewers.sq3"
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()


    cur.execute("SELECT * FROM viewers")
    conn.commit()
    output_sql = list(cur)

    #print(output_sql)

    print("done")

    get_profile = output_sql[0]
    print(get_profile)

    #name = get_profile[1]

    root = Tk()
    t = Text(root)

    for i,elt in enumerate(output_sql):
        print(elt[1])


        t.insert(END,elt[1] + '\n')
    t.pack()
    root.mainloop()
