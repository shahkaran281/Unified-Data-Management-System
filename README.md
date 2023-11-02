# DSCI551-Project
Project for DSCI 551 - Foundation of Data Managment. The objective is to create SQL and NoSQL for scratch.



## Aggregate Example

AGGREGATE COUNT(channel_type) , Title, rank  ,  category FROM YouTubeChannel GROUP BY Title

## Here Group By is an optional attribute

AGGREGATE COUNT(channel_type) , Title, rank  ,  category FROM YouTubeChannel

## Example for Group By , Condition and Order By

SELECT Title, rank , Country FROM YouTubeChannel WHERE rank == '9'

SELECT Title, rank , Country FROM YouTubeChannel ORDER BY Country

SELECT Title, rank , Country FROM YouTubeChannel WHERE rank > '1' GROUP BY Country ORDER BY Country