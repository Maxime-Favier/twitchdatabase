first_run = 0
debug = 1

    # check if that is the first run
    try:
        config = open("graphical-interface/config/first-run-graph.conf", "r")

    except FileNotFoundError:

        if debug == 1:
             print("first run!")

        config = open("graphical-interface/config/first-run-graph.conf", "w")
        config.write("first-run = true")
        first_run = 1




