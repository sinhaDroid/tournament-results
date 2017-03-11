#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db, cursor()
        return db, cursor
    except:
        print("Connection Error")
    #return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    cursor.execute("DELETE FROM matches *;")
    db.commit()
    db.close()
    # connection = connect()
    # cursor = connection.cursor()
    # cursor.execute("DELETE FROM matches *;")
    # connection.commit()
    # connection.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    cursor.execute("DELETE FROM players *;")
    db.commit()
    db.close()
    
    #connection = connect()
    #cursor = connection.cursor()
    #cursor.execute("DELETE FROM players *;")
    #connection.commit()
    #connection.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()

    query = "SELECT count(*) FROM players;"
    cursor.execute(query)
    numberPlayers = cursor.fetchall()[0][0]

    db.commit()
    db.close()
    #connection = connect()
    #cursor = connection.cursor()
    #cursor.execute("SELECT count(*) FROM players;")
    #numberPlayers = cursor.fetchall()[0][0]
    #connection.commit()
    #connection.close()

    return numberPlayers


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()

    # query = "INSERT INTO players (name) VALUES (%s);"
    parameter = (name,)
    cursor.execute("INSERT INTO players (name) VALUES (%s);", parameter)

    db.commit()
    db.close()
    #connection = connect()
    #cursor = connection.cursor()
    #cursor.execute("INSERT INTO players (name) VALUES (%s);", (name,))
    #connection.commit()
    #connection.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    cursor.execute("SELECT * FROM standings")
    standings = cursor.fetchall()
    db.close()
    # connection = connect()
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM standings")
    # standings = cursor.fetchall()
    # connection.close()

    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    db, cursor = connect()
    cursor.execute(("INSERT INTO matches (player_1, player_2, winner)"
                    "VALUES (%s,%s,%s);"),
                   ((winner,), (loser,), (winner,)))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    parings = []
    rankedPlayerList = playerStandings()
    i = 0
    while i < len(rankedPlayerList):
        parings.append((rankedPlayerList[i][0],
                        rankedPlayerList[i][1],
                        rankedPlayerList[i + 1][0],
                        rankedPlayerList[i + 1][1]))
        i += 2
    return parings
