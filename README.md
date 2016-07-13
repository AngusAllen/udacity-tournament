# udacity-tournament
Project assignment for Udacity IPND program, stage 5 (back-end developer)

##Summary

This is a simple database project for Udacity's IPND course "introduction to back-end prgramming".  The project requires the creation of a PostgreSQL database to manage a Swiss style gaming tournament.

## Requirements

This software has been designed to be used in the VM enironment provided by Udacity using Oracle's VM Virtual Box and Vagrant.  You can fork/clone this by accessing this [GitHub repo](https://github.com/udacity/fullstack-nanodegree-vm).

If you are not using the above environment, the requirements are as follows:

* Python 2.7
* Bleach sanitising library
* PostgreSQL CLI 
* Psycopg2 postgreSQL database adaptor for Python

##Usage

**1.  Download files**

**2. Create database**

Log into your PostgreSQL console.  Executing the following command will create the database, connect to it and create the tables schema:

`\i tournament.sql`

**3.  Import functions**

To run the tournament you need to call the tournament functions.  Accordingly, import the file entitled tournament.py into your python script.

`import tournament.py`

**4.  Use the functions**

The following functions are included in tournament.py for you to use in running the tournament.

**connect()**

Connects to the PostgreSQL database and returns a database connection.

**deleteMatches()**

Remove all match records from the database.

**deletePlayers()**

Remove all player records from the database.

**countPlayers()**

Returns the number of players currently registered in the tournament.

**registerPlayer(name)**

Adds a player to the tournament database. The database assigns a unique serial id number for each player.

**playerStandings()**

Returns a list of the players and their win records, sorted by wins. Therefore, the first entry is the player in first place or a player tied for first place if there is a tie.

**reportMatch(winner,loser)**

Creates a new match record, recording the winner and the loser of the match. The arguments for the winner and the loser must be the id numbers for each player.

**swissPairings()**

Returns a list containing pairs of players for the next round. The function assumes an even number of players registered and pairs players based on an equal or nearly-equal win record.

##Limitations

* Number of players (n) entering the tournament must be even and n to a power 
* Does not support multiple tournaments
* Does not support draws between players

##Licence

This project is a public domain work, dedicated using [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Feel free to do whatever you want with it.
