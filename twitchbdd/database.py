#!/usr/bin/env python
# -*-coding:Latin-1 -*
"""module database: check if the pseudo is in the bdd, add the user points"""
import sqlite3
import time
import os

first_run = 0

try:
    config = open("config/first-run.conf", "r")
except:
    print("first run!")
    config = open("config/first-run.conf", "w")
    config.write("first-run = true")
    first_run = 1

finally:

    debug = 1
    pseudo = 'emeric75'

    database_path = "database/viewers.sq3"
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    if first_run == 1:

        if debug == 1:
            print("creating database")

        cur.execute("CREATE TABLE viewers ("
                    " id INTEGER NOT NULL PRIMARY KEY,"
                    " name TEXT, point INTEGER,"
                    " avert INTEGER,"
                    " lastsee DATETIME,"
                    " firsttime DATETIME)")
        cur.execute("INSERT INTO viewers(id,name,point,avert,lastsee,firsttime)"
                    " VALUES(NULL,'maxime_le_goupil', 10, 0, '2000-01-01 0:0:0', '2000-01-01 0:0:0')")
        conn.commit()

        if debug == 1:
            print("database created")

    sql_input = pseudo,
    cur.execute("SELECT * FROM viewers WHERE name LIKE ?", sql_input)
    conn.commit()

    output_sql = list(cur)

    if debug == 1:
        print(output_sql)

    if output_sql == []:
        # add viewer in the database

        if debug == 1:
            print("preparing to add a new user in the database: ", pseudo)

        last_see = time.strftime("%Y-%m-%d %H:%M:%S")
        sql_input = (pseudo, 10, 0, last_see, last_see)

        cur.execute("INSERT INTO viewers (id, name, point, avert, lastsee, firsttime)"
                    " VALUES (NULL, ?, ?, ?, ?, ?)", sql_input)
        conn.commit()

        if debug == 1:
            print("successfully add a new user")

    else:

        if debug == 1:
            print("old user detected")

        get_points = output_sql[0]
        list_sql = list(get_points)
        new_points = list_sql[2] + 10

        if debug == 1:
            print("new balance",new_points)

        last_see = time.strftime("%Y-%m-%d %H:%M:%S")
        sql_input = (new_points, pseudo)
        cur.execute("UPDATE viewers SET point = ? WHERE name = ?", sql_input)
        conn.commit()

        sql_input = (last_see, pseudo)
        cur.execute("UPDATE viewers SET lastsee = ? WHERE name = ?", sql_input)
        conn.commit()



    cur.close()
    conn.close()
