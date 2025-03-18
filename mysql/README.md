# DSCI 551 - MySQL Database

## SQL Query Language
This section details the SQL commands used in the hybrid database system.

### **CREATE TABLE COMMAND**
```sql
CREATE TABLE newTable (id, name, val)
```

### **INSERT INTO TABLE COMMAND**
```sql
INSERT INTO newTable (100, John Doe, 1000)
INSERT INTO newTable (101, Jake Doe, 2000)
INSERT INTO newTable (201, Sal Doe, 2000)
INSERT INTO newTable (301, Sal Doe , 3000)
```

### **UPDATE COMMAND**
```sql
UPDATE INTO newTable 9431fa9d-9cbf-4284-9496-e0e99657e32f ( id 999 , val 420)
```

### **DELETE COMMAND**
```sql
DELETE FROM newTable efca5fe7-a9b4-4bc7-a1d9-46af45ac3f5e
```

### **FILTER COMMANDS**
```sql
Filter [ Youtuber,subscribers] from YoutubeChannel where rank >= 5
```

### **PROJECTION COMMANDS**
```sql
Proj [uuid, rank, Youtuber ] FROM YoutubeChannels
```

### **JOIN COMMANDS**
```sql
Join ['Youtuber'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fk WHERE country_rank >= 5 ORDER BY Youtuber
```

### **AGGREGATE COMMANDS**
```sql
AGGREGATE COUNT(channel_type) , Title, rank , category FROM YoutubeChannels GROUP BY Title
AGGREGATE COUNT(channel_type) , Title, rank , category FROM YoutubeChannels
```

### **GROUP, CONDITION AND ORDER BY**
```sql
SELECT Title, rank , Country FROM YoutubeChannels WHERE rank == '9'
SELECT Title, rank , Country FROM YoutubeChannels ORDER BY Country
SELECT Title, rank , Country FROM YoutubeChannels WHERE rank > '1' GROUP BY Country ORDER BY Country
```


## License
This project is open-source and available under the [MIT License](LICENSE).
