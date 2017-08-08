# -*-coding:Latin-1 -*
# /usr/bin/python3

"""module databas: check if the pseudo is in the bdd, add the user points"""


def processdata(pseudo, debug = 0):

    import time

    try:
        import sqlite3      # sql package

    except ImportError:
        raise ImportError("unable to find lib: sqlite3 and/or time")

    first_run = 0

    # check if that is the first run
    try:
        config = open("config/first-run.conf", "r")

    except FileNotFoundError:
        print("first run!")
        config = open("config/first-run.conf", "w")
        config.write("first-run = true")
        first_run = 1

    finally:

        # connect to the database
        database_path = "database/viewers.sq3"
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()

        if first_run == 1:
            # create database

            if debug == 1:
                print("creating database")

            try:
                # create sql table
                cur.execute("CREATE TABLE viewers ("
                        " id INTEGER NOT NULL PRIMARY KEY,"
                        " name TEXT, point INTEGER,"
                        " avert INTEGER,"
                        " lastsee DATETIME,"
                        " firsttime DATETIME)")
                # just a test sample
                cur.execute("INSERT INTO viewers(id,name,point,avert,lastsee,firsttime)"
                        " VALUES(NULL,'maxime_le_goupil', 10, 0, '2000-01-01 0:0:0', '2000-01-01 0:0:0')")
                # execute sql request
                conn.commit()

            except:
                raise Exception("sql creation error")

            if debug == 1:
                print("database created")

        sql_input = pseudo,

        try:
            # find the viewer in the database
            cur.execute("SELECT * FROM viewers WHERE name LIKE ?", sql_input)
            conn.commit()

        except:
            raise Exception('sql find error')

        output_sql = list(cur)

        if debug == 1:
            print(output_sql)

        if output_sql == []:
            # add viewer in the database

            if debug == 1:
                print("preparing to add a new user in the database: ", pseudo)

            last_see = time.strftime("%Y-%m-%d %H:%M:%S")
            sql_input = (pseudo, 10, 0, last_see, last_see)

            try:
                cur.execute("INSERT INTO viewers (id, name, point, avert, lastsee, firsttime)"
                        " VALUES (NULL, ?, ?, ?, ?, ?)", sql_input)
                conn.commit()

            except:
                raise Exception('sql create user error')

            if debug == 1:
                print("successfully add a new user")

        else:
            # change the number of point and the lastsee date
            if debug == 1:
                print("old user detected")

            # get the old amount of point
            get_points = output_sql[0]
            list_sql = list(get_points)
            new_points = list_sql[2] + 10

            if debug == 1:
                print("new balance", new_points)

            last_see = time.strftime("%Y-%m-%d %H:%M:%S")
            sql_input = (new_points, pseudo)

            try:
                # change the amount of point
                cur.execute("UPDATE viewers SET point = ? WHERE name = ?", sql_input)
                conn.commit()

            except:
                raise Exception('sql set points error')

            sql_input = (last_see, pseudo)

            try:
                # change
                cur.execute("UPDATE viewers SET lastsee = ? WHERE name = ?", sql_input)
                conn.commit()
            except:
                raise Exception('sql set lastsee error')

        cur.close()
        conn.close()
