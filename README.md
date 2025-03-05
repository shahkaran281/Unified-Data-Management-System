## NO SQL Commands

## CREATE TABLE COMMAND

CREATE TABLE ZZ

## INSERT INTO TABLE COMMAND

INSERT INTO ZZ ({"id":"1"})
INSERT INTO ZZ ({"id":"1" , "value" : "Test"})

## UPDATE ZZ

UPDATE INTO ZZ 9749f911-75bb-48a5-9475-61b107bcff26 ({"id" : "99" , "value": "updated"})

## DELETE COMMAND

DELETE FROM ZZ 9749f911-75bb-48a5-9475-61b107bcff26

## FILTER COMMAND

filter all from youtube_data

filter all from youtube_data where rank >= 5

filter [channel_name,subscribers] from youtube_data

filter [channel_name,subscribers] from youtube_data where rank >= 5

## JOIN COMMAND

Join ['name', 'age'], ['job', 'city'] FROM Table1.uuid = Table2.fk

Join ['name', 'age'], ['job', 'city'] FROM Table1.uuid = Table2.fk Where age > 25

Join ['name', 'age'], ['job', 'city'] FROM Table1.uuid = Table2.fk Where age > 25 order by city
