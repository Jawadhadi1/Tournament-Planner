#Implementation of the Swiss System Tournament

import psycopg2


def close_cursor_and_connection(cursor, connection):
    """Close cursor and connection objects"""
    cursor.close()
    connection.close()


def get_cursor_and_connection():
    """Returns database connection and cursor objects"""
    connection = psycopg2.connect("dbname=tournament")
    return connection, connection.cursor()


def register_player(name):
    """Adds a player to the tournament database.
       The argument name need not be unique as the database assigns a unique ID
       to every player"""
    
    connection, cursor = get_cursor_and_connection()
    cursor.execute("INSERT INTO Players (Name) VALUES(%s)", (name,))
    connection.commit()
    close_cursor_and_connection(cursor, connection)

def count_players():
    """Returns the number of players which are currently registered."""
    connection, cursor = get_cursor_and_connection()
    cursor.execute("SELECT COUNT(PlayerID) FROM Players;")
    count = cursor.fetchone()[0]
    close_cursor_and_connection(cursor, connection)
    return count

def delete_players():
    """Remove all the player records which are currently present in the
    database."""
    connection, cursor = get_cursor_and_connection()
    cursor.execute("DELETE FROM Players;")
    connection.commit()
    close_cursor_and_connection(cursor, connection)

def report_match(winner, loser):
    """Records the outcome of a single match between the two players.
    Arguments:
      winner: the id number of the player who won the match
      loser:  the id number of the player who lost the match
    """
    connection, cursor = get_cursor_and_connection()
    cursor.execute("INSERT INTO Matches VALUES(%s, %s)", (winner, 'Win'))
    cursor.execute("INSERT INTO Matches VALUES(%s, %s)", (loser, 'Loss'))
    connection.commit()
    close_cursor_and_connection(cursor, connection)

def delete_matches():
    """Remove all the match records present in the database."""
    connection, cursor = get_cursor_and_connection()
    cursor.execute("DELETE FROM Matches;")
    connection.commit()
    close_cursor_and_connection(cursor, connection)    

def player_standings():
    """Returns a list of the players and their win records, sorted by the number of wins.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches) where:
        id: the player's unique id which is assigned by the database
        name: the player's full name 
        wins: the total number of matches the player has won
        matches: the total number of matches the player has played"""
    
    query = """
                (SELECT Playerss.PlayerID, Playerss.Name,
                FROM Players Playerss
         LEFT JOIN (
                     SELECT Matchess.PlayerID, COUNT(Matchess.Result) as wincount
                     FROM Matches Matchess
                     WHERE Matchess.Result = 'Win'
                     GROUP By Matchess.PlayerID
                   ) Matcheswin
                    ON Playerss.PlayerID=Matcheswin.PlayerID
                 ) WinTable
                LEFT JOIN
                    (
                    SELECT Matchess.PlayerID,
                    COUNT(Matchess.Result) as matchcount
                    FROM Matches Matchess
                    GROUP BY Matchess.PlayerID
                    ) Matchess
                ON WinTable.PlayerID=Matchess.PlayerID
                ORDER By WinTable.wincount Desc;"""

    connection, cursor = get_cursor_and_connection()
    cursor.execute(query)
    output = cursor.fetchall()
    close_cursor_and_connection(cursor, connection)

    return output

def swiss_pairings():
    """ Each player is paired with another
    player with an equal or a nearly equal win record; a player adjacent
    to him in the rankings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2) where:
        id1: the first player's id
        name1: the first player's name
        id2: the second player's id
        name2: the second player's name"""
    
    rankings = player_standings()
    players_pairings = []
    players_paired = []
    for player in rankings:
        # the len for each player is 2 because id and name are used for each player
        if len(players_paired) < 4:
            players_paired.append(player[0])
            players_paired.append(player[1])
        # when len == 4, the 2 players are paired
        if len(players_paired) == 4:
            players_pairings.append(tuple(players_paired))
            players_paired = []

    return players_pairings
