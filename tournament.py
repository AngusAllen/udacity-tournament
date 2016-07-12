#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from bleach import clean

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute('DELETE FROM matches')
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute('DELETE FROM players')
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute('SELECT COALESCE(count(*),0) FROM players')
    rows = c.fetchall()
    db.close()
    for row in rows:
        result = row[0]
    return result

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute('INSERT INTO players (player_name) VALUES (%s)', (name,))
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    standings = []
    db = connect()
    c = db.cursor()
    """Query to be executed below joins two new tables with the following names:
        "win_rank"
        "loss_count"

    "win_rank" is itself the output table from a join of a new table
    named "win_count" on the table "players"
    """
    c.execute('SELECT '
            '       win_rank.id, '
            '       win_rank.name, '
            '       win_rank.wins, '
            '       COALESCE(loss_count.losses, 0) AS losses '
            'FROM '
            '       (SELECT players.player_id AS id, '
            '           players.player_name AS name, '
            '           COALESCE(win_count.wins, 0) AS wins '
            '        FROM '
            '           (SELECT winner_id, '
            '           COUNT(winner_id) AS wins '
            '           FROM matches '
            '           GROUP BY winner_id) AS win_count '
            '        FULL OUTER JOIN '
            '           players '
            '        ON players.player_id = win_count.winner_id) AS win_rank '
            'FULL OUTER JOIN '
            '        (SELECT loser_id, '
            '           COUNT(loser_id) AS losses '
            '        FROM matches '
            '        GROUP BY loser_id) AS loss_count '
            'ON win_rank.id = loss_count.loser_id '
            'ORDER BY win_rank.wins DESC')

    rows = c.fetchall()
    db.close()
    for row in rows:
        total_matches = int(row[2]) + int(row[3])
        player_tuple = (row[0],row[1],int(row[2]),total_matches)
        standings.append(player_tuple)
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    c.execute('INSERT INTO matches (winner_id, loser_id) '
            ' VALUES (%s, %s)', (winner, loser,))
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
    standings = playerStandings()
    num = int(countPlayers())
    pairings = []
    players_per_match = 2
    next_in_standings = 1
    if num > 0:
        for i in range (num):
            if i % players_per_match == 0:
                id1 = standings[i][0]
                name1 = standings[i][1]
                id2 = standings[i+next_in_standings][0]
                name2 = standings[i+next_in_standings][1]
                pair = (id1, name1, id2, name2)
                pairings.append(pair)
    return pairings
