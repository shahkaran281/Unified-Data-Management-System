# DSCI551-Project
Project for DSCI 551 - Foundation of Data Managment. The objective is to create SQL and NoSQL for scratch.



## Aggregate Example

AGGREGATE COUNT(channel_type) , Title, rank  ,  category FROM YoutubeChannels GROUP BY Title

## Here Group By is an optional attribute

AGGREGATE COUNT(channel_type) , Title, rank  ,  category FROM YoutubeChannels

## Example for Group By , Condition and Order By

SELECT Title, rank , Country FROM YoutubeChannels WHERE rank == '9'

SELECT Title, rank , Country FROM YoutubeChannels ORDER BY Country

SELECT Title, rank , Country FROM YoutubeChannels WHERE rank > '1' GROUP BY Country ORDER BY Country




CREATE TABLE newTable (id,name)
CREATE TABLE newTable ( id,  name)
CREATE TABLE newTable ( id,  name, val)
CREATE TABLE      newTable ( id,  name, val)

INSERT INTO newTable (100, John Doe, 1000)
INSERT INTO newTable (101, Jake Doe, 2000)
INSERT INTO newTable (201, Sal Doe, 2000)
INSERT INTO newTable (301,    Sal Doe   , 3000)


UPDATE INTO newTable 9431fa9d-9cbf-4284-9496-e0e99657e32f ( id 999 , val 420)

DELETE FROM newTable efca5fe7-a9b4-4bc7-a1d9-46af45ac3f5e
DELETE FROM newTable       efca5fe7-a9b4-4bc7-a1d9-46af45ac3f5e
DELETE FROM newTable       efca5fe7-a9b4-4bc7-a1d9-46af45ac3f52 (From value not present in table)

Filter [  Youtuber,subscribers] from YoutubeChannel where rank >= 5
Filter [  Youtuber,   subscribers] from YoutubeChannels where rank >= 5
Filter [  Youtuber,   subscribers]     from YoutubeChannels    where rank >= 5

Proj [uuid, rank, Youtuber ] FROM YoutubeChannels
Proj [uuid, ranks, Youtuber ] FROM YoutubeChannels
Proj [uuid, rank, Youtuber ] FROM YoutubeChannel
 
Join ['Youtuber'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fk WHERE country_rank >= 5 ORDER BY Youtuber
// Errors
Join ['Youtubers'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fk WHERE country_rank >= 5 ORDER BY Youtuber
Join ['Youtuber'], ['video_views_ranks','country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fk WHERE country_rank >= 5 ORDER BY Youtuber
Join ['Youtuber'], ['video_views_ranks','country_rank'] FROM YoutubeChannel.uuid = YoutubeViews.fk WHERE country_rank >= 5 ORDER BY Youtuber
Join ['Youtuber'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuids = YoutubeViews.fk WHERE country_rank >= 5 ORDER BY Youtuber
Join ['Youtuber'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuid = YoutubeView.fk WHERE country_rank >= 5 ORDER BY Youtuber
Join ['Youtuber'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fkey WHERE country_rank >= 5 ORDER BY Youtuber
Join ['Youtuber'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fk WHERE country_ranks >= 5 ORDER BY Youtuber
Join ['Youtuber'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fk WHERE country_rank >= 10 ORDER BY Youtuber 
** Last one is showing incorrect output