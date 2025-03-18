# DSCI 551 - Hybrid Database System

## Project Overview
This project involves designing and implementing a hybrid database system that integrates both SQL and NoSQL data models. The system will handle YouTube analytics data using a relational database and Air Traffic Landing statistics at San Francisco International Airport (SFO) using a NoSQL database.

## System Design
### 1. Relational Model (SQL)
**Dataset:** [YouTube Global Statistics 2023](https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023)

- **Entities:**
  - Creator
  - Video Statistics
  - Country Details
  - Subscribers
  - Monetary Statistics
- **Implementation Details:**
  - Data is extracted, filtered, and normalized into relational tables.
  - A Python-based custom key-value store enables efficient joins and projections.
  - UUIDs ensure uniqueness and prevent hash conflicts.

### 2. Non-Relational Model (NoSQL)
**Dataset:** [SFO Air Traffic Landing Statistics](https://www.kaggle.com/datasets/lostinworlds/sf-air-traffic-landing-statistics)

- **Collections:**
  - Airlines
  - AirportRegions
  - AircraftDetails
- **Implementation Details:**
  - Data is stored in JSON format, simulating NoSQL collections.
  - Schema is adjustable on the fly for flexibility.

## Query Language
The system includes a custom query language supporting:

### **NoSQL Commands**
#### **CREATE TABLE COMMAND**
```sql
CREATE TABLE ZZ
```

#### **INSERT INTO TABLE COMMAND**
```sql
INSERT INTO ZZ ({"id":"1"})
INSERT INTO ZZ ({"id":"1" , "value" : "Test"})
```

#### **UPDATE COMMAND**
```sql
UPDATE INTO ZZ 9749f911-75bb-48a5-9475-61b107bcff26 ({"id" : "99" , "value": "updated"})
```

#### **DELETE COMMAND**
```sql
DELETE FROM ZZ 9749f911-75bb-48a5-9475-61b107bcff26
```

#### **FILTER COMMAND**
```sql
filter all from youtube_data
filter all from youtube_data where rank >= 5
filter [channel_name,subscribers] from youtube_data
filter [channel_name,subscribers] from youtube_data where rank >= 5
```

#### **JOIN COMMAND**
```sql
Join ['name', 'age'], ['job', 'city'] FROM Table1.uuid = Table2.fk
Join ['name', 'age'], ['job', 'city'] FROM Table1.uuid = Table2.fk Where age > 25
Join ['name', 'age'], ['job', 'city'] FROM Table1.uuid = Table2.fk Where age > 25 order by city
```

#### **AGGREGATE COMMANDS**
```sql
AGGREGATE COUNT(channel_type) , Title, rank , category FROM YoutubeChannels GROUP BY Title
AGGREGATE COUNT(channel_type) , Title, rank , category FROM YoutubeChannels
```

#### **GROUP, CONDITION AND ORDER BY**
```sql
SELECT Title, rank , Country FROM YoutubeChannels WHERE rank == '9'
SELECT Title, rank , Country FROM YoutubeChannels ORDER BY Country
SELECT Title, rank , Country FROM YoutubeChannels WHERE rank > '1' GROUP BY Country ORDER BY Country
```

### **SQL Commands**
#### **CREATE TABLE**
```sql
CREATE TABLE newTable (id, name, val)
```

#### **INSERT INTO TABLE**
```sql
INSERT INTO newTable (100, John Doe, 1000)
INSERT INTO newTable (101, Jake Doe, 2000)
INSERT INTO newTable (201, Sal Doe, 2000)
INSERT INTO newTable (301, Sal Doe , 3000)
```

#### **UPDATE TABLE**
```sql
UPDATE INTO newTable 9431fa9d-9cbf-4284-9496-e0e99657e32f ( id 999 , val 420)
```

#### **DELETE FROM TABLE**
```sql
DELETE FROM newTable efca5fe7-a9b4-4bc7-a1d9-46af45ac3f5e
```

#### **FILTER COMMANDS**
```sql
Filter [ Youtuber,subscribers] from YoutubeChannel where rank >= 5
```

#### **PROJECTION COMMANDS**
```sql
Proj [uuid, rank, Youtuber ] FROM YoutubeChannels
```

#### **JOIN COMMANDS**
```sql
Join ['Youtuber'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fk WHERE country_rank >= 5 ORDER BY Youtuber
```

**Note:** The last join query is showing incorrect output, further debugging may be required.

## Team Members
### **Karan Manishkumar Shah**
- **Role:** NoSQL Database Specialist
- **Skills:** NoSQL systems, data modeling, data integration
- **Responsibilities:**
  - Implement NoSQL database structure
  - Define schema and queries
  - Ensure data consistency and scalability

### **Aniket Kumar**
- **Role:** SQL Database Specialist
- **Skills:** SQL, relational schema design, query optimization
- **Responsibilities:**
  - Implement relational database schema
  - Optimize SQL queries
  - Develop stored procedures



## License
This project is open-source and available under the [MIT License](LICENSE).
