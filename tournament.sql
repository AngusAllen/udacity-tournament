-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
--
-- Notes:
-- Start with statements: create database tournament; \c tournament; \i tournament.sql;

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

DROP TABLE IF EXISTS players;
CREATE TABLE players(
  player_id SERIAL PRIMARY KEY,
  player_name VARCHAR (25) NOT NULL
);

DROP TABLE IF EXISTS matches;
CREATE TABLE matches(
  match_id SERIAL PRIMARY KEY,
  -- winner_id is the serial_id of the winning player
  winner_id INTEGER REFERENCES players(player_id),
  -- loser_id is the serial_id of the losing player
  loser_id INTEGER REFERENCES players(player_id)
);
