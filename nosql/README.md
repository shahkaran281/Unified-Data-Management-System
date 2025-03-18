# DSCI 551 - MySQL README

## SQL Query Language Overview
This section details the SQL commands used in the hybrid database system, designed to efficiently manage structured YouTube analytics data.

### **Table Creation**
```sql
CREATE TABLE newTable (id INT, name VARCHAR(255), val INT);
```

### **Data Insertion**
```sql
INSERT INTO newTable (id, name, val) VALUES (100, 'John Doe', 1000);
INSERT INTO newTable (id, name, val) VALUES (101, 'Jake Doe', 2000);
INSERT INTO newTable (id, name, val) VALUES (201, 'Sal Doe', 2000);
```

### **Updating Records**
```sql
UPDATE newTable SET id = 999, val = 420 WHERE id = 9431fa9d-9cbf-4284-9496-e0e99657e32f;
```

### **Deleting Records**
```sql
DELETE FROM newTable WHERE id = 'efca5fe7-a9b4-4bc7-a1d9-46af45ac3f5e';
```

### **Filtering Data**
```sql
SELECT Youtuber, subscribers FROM YoutubeChannel WHERE rank >= 5;
```

### **Projection Queries**
```sql
SELECT uuid, rank, Youtuber FROM YoutubeChannels;
```

### **Join Queries**
```sql
SELECT Youtuber, video_views_rank, country_rank
FROM YoutubeChannels
JOIN YoutubeViews ON YoutubeChannels.uuid = YoutubeViews.fk
WHERE country_rank >= 5
ORDER BY Youtuber;
```

### **Aggregation Queries**
```sql
SELECT COUNT(channel_type), Title, rank, category 
FROM YoutubeChannels 
GROUP BY Title;
```

### **Grouping, Conditions & Ordering**
```sql
SELECT Title, rank, Country FROM YoutubeChannels WHERE rank = 9;
SELECT Title, rank, Country FROM YoutubeChannels ORDER BY Country;
SELECT Title, rank, Country FROM YoutubeChannels WHERE rank > 1 GROUP BY Country ORDER BY Country;
```

## License
This project is open-source and available under the [MIT License](LICENSE).
