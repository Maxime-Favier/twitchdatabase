# -*-coding:Latin-1 -*
# !/usr/bin
"""module mysqlfind: check if the pseudo is in the bdd"""


def mysqlfind(pseudo, user, password, host='localhost', database='twitchbdd', debug=0):

    try:
        import mysql.connector

    except:
        raise ModuleNotFoundError("unable to load lib: mysql.connector")

    cnx = mysql.connector.connect(user, password, host, database)
    cursor = cnx.cursor()

    #query = ("SELECT * FROM `viewers` WHERE `name` LIKE '%s'")
    #cursor.execute(query, (pseudo))

    #print(cursor)

    cnx.close()

mysqlfind("maxime_le_goupil", "python-client", "python", 'localhost', 'twitchbdd', 0)