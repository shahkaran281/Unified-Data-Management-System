## NO SQL Commands 

## CREATE TABLE COMMAND

CREATE TABLE ZZ

## INSERT INTO TABLE COMMAND

INSERT INTO ZZ ({"id":"1"})
INSERT INTO ZZ ({"id":"1" , "value" : "Test"})


## UPDATE ZZ

UPDATE INTO ZZ 9749f911-75bb-48a5-9475-61b107bcff26 ({"id" : "99" , "value": "updated"}))


## DELETE COMMAND

DELETE FROM ZZ 9749f911-75bb-48a5-9475-61b107bcff26

## SELECT AND FILTER OPERATIONS

SELECT Activity_Period , GEO_Summary , GEO_Region FROM airline WHERE GEO_Region == "Caribbean" ORDER BY Activity_Period


AGGREGATE COUNT(Operating_Airline) , GEO_Region FROM airline GROUP BY GEO_Region ORDER BY GEO_Region




