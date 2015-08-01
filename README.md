# **Tournament Planner**


### **About**
This project uses the PostgreSQL database to keep track of players and matches in a game tournament. The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player would be paired with another player with the same number of wins, or as close as possible.
This project has two parts: defining the database schema (SQL table definitions), and the code that will use it. 

### **Language**
Python

### **Tasks/Functions/Requirements Implemented**

**registerPlayer(name)**

Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

**countPlayers()**

Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

**deletePlayers()**

Clear out all the player records from the database.

**reportMatch(winner, loser)**

Stores the outcome of a single match between two players in the database.

**deleteMatches()**

Clear out all the match records from the database.

**playerStandings()**

Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

**swissPairings()**

Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.

### **Setup Instructions**

1.	First download and then install the python 2.7 module in your system.

2.	Download and install the PostgreSQL database.

3.	Download and install the PostgreSQL adapter for Python programming language Psycopg2.

4.	Run the tournament_test.py file in order to test the functionalities of the program. 




