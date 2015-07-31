-- Definitions of the tables used in the project





CREATE TABLE Players(PlayerID serial primary key, Name varchar(100));






CREATE TABLE Matches(PlayerID serial references Players, Result varchar(10));
