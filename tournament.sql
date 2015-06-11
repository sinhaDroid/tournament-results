-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create tables for the tournament database.

CREATE TABLE players (
    id serial PRIMARY KEY,
    name text
);

CREATE TABLE matches (
	player_1 integer REFERENCES players,
	player_2 integer REFERENCES players,
	winner integer REFERENCES players
);

-- Create some views to make it easy to get player standings.

-- matches_count will get us the number of matches a player has competed in. This will be used when we get our standings.

CREATE VIEW matches_count AS
    SELECT (
    	SELECT count(*) 
    	FROM matches
    	) /
    	(SELECT count(*) / 2
    	FROM players
    	) AS round_count;

-- standings is a view to make it easier to grab our standings out of the database. 

CREATE VIEW standings AS
    SELECT players.id, players.name, count(matches.winner) AS num, (SELECT * FROM matches_count) as num_matches
    FROM players LEFT JOIN matches
    ON players.id = matches.winner
    GROUP BY players.id
    ORDER BY num DESC;
  

