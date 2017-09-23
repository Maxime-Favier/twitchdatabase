from graphicalinterface.channelselect import *
from tkinter import *

first_run = 0
debug = 1

# check if that is the first run
try:
    config = open("graphicalinterface/config/first-run-graph.conf", "r")

except FileNotFoundError:

    if debug == 1:
        print("first run!")
    config = open("graphicalinterface/config/first-run-graph.conf", "w")
    config.write("first-run = true")
    first_run = 1

finally:
    # Get the new user channel name
    pseudo = channelselect(1)
    print("done")
    print(pseudo)





