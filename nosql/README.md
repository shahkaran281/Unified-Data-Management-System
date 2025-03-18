# DSCI 551 - NoSQL README

## NoSQL Query Language Overview
This section details the NoSQL commands used in the hybrid database system, designed to efficiently manage flexible air traffic landing data.

### **Table Creation**
```nosql
CREATE TABLE ZZ;
```

### **Data Insertion**
```nosql
INSERT INTO ZZ ( {"id":"1"} );
INSERT INTO ZZ ( {"id":"1", "value":"Test"} );
```

### **Updating Records**
```nosql
UPDATE INTO ZZ 9749f911-75bb-48a5-9475-61b107bcff26 ( {"id":"99", "value":"updated"} );
```

### **Deleting Records**
```nosql
DELETE FROM ZZ 9749f911-75bb-48a5-9475-61b107bcff26;
```

### **Filtering Data**
```nosql
filter all from youtube_data;
filter all from youtube_data where rank >= 5;
filter [channel_name, subscribers] from youtube_data;
filter [channel_name, subscribers] from youtube_data where rank >= 5;
```

### **Join Queries**
```nosql
Join ['name', 'age'], ['job', 'city'] FROM Table1.uuid = Table2.fk;
Join ['name', 'age'], ['job', 'city'] FROM Table1.uuid = Table2.fk WHERE age > 25;
Join ['name', 'age'], ['job', 'city'] FROM Table1.uuid = Table2.fk WHERE age > 25 ORDER BY city;
```

### **Aggregation Queries**
```nosql
AGGREGATE COUNT(channel_type), Title, rank, category FROM YoutubeChannels GROUP BY Title;
```

### **Grouping, Conditions & Ordering**
```nosql
SELECT Title, rank, Country FROM YoutubeChannels WHERE rank = 9;
SELECT Title, rank, Country FROM YoutubeChannels ORDER BY Country;
SELECT Title, rank, Country FROM YoutubeChannels WHERE rank > 1 GROUP BY Country ORDER BY Country;
```


## License
This project is open-source and available under the [MIT License](LICENSE).
