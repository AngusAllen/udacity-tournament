# udacity-tournament
Project assignment for Udacity IPND program, stage 5 (back-end developer)

INTRODUCTION

This project provides a way to keep track of players and matches in a swiss style tournament with an even number of players and without any player requiring a bye.  Here, any given match can result in a win or a loss.  The pairing function ensures that in the next round a player is paired with a player of a similar level.  All information is stored in a Postgres database.  Since there are several ways in which user input can make its way directly into the database, all inputs are checked to ensure they are free from bugs before being used.

REQUIREMENTS

- Python 2.7

- Bleach

- Psycopg2

- PostgreSQL

INSTALLATION AND DATABASE SET-UP

Ideally this tournament should be operated using the VirtualBox and Vagrant VM provided by Udacity.

Navigate to the cloned tournament depository in a shell.  Please make sure that you have a psql user with database creation permissions set up.  Run the following command in the psql CLI: psql -f tournament.sql.  This sets up and then connects to a fresh tournament database with the schema laid out in the file tournament.sql. Please note that the tournament.sql file includes instructions to create the database "tournament" and to connect to it.

USAGE

You can register players into the database with registerPlayer(name) by providing the name of the player.  In this instance, you will need to have a number of players equal to 2 to a chosen power.  At any point you can check the standings with playerStandings() and get a ranked list of the players with their respective ID, name, number of wins and number of matches.  The swissPairings() function should be run at the start of a new round to determine which players should play one another.
