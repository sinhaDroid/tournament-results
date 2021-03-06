-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- 

CREATE TABLE players (
    id serial PRIMARY KEY,
    name text
);

CREATE TABLE matches (
    match_id serial PRIMARY KEY,
	player_1 integer REFERENCES players,
	player_2 integer REFERENCES players,
	winner INT REFERENCES players(id)
);



CREATE VIEW matches_count AS
    SELECT (
    	SELECT count(*) 
    	FROM matches
    	) /
    	(SELECT count(*) / 2
    	FROM players
    	) AS round_count;

CREATE VIEW standings AS
    SELECT players.id, players.name, count(matches.winner) AS num, (SELECT * FROM matches_count) as num_matches
    FROM players LEFT JOIN matches
    ON players.id = matches.winner
    GROUP BY players.id
    ORDER BY num DESC;
    
