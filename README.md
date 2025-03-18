# DSCI 551 - Project Structure

## Summary
This project provides a unified query interface for both **SQL and NoSQL** databases, enabling seamless interactions through a structured command-line interface. It efficiently processes **CSV-based relational data** and **JSON-based document data** while supporting **complex queries, joins, and aggregations**.

## Folder Organization
The project is divided into two main components:
- **`mysql/`** - Contains all SQL-related functionality.
- **`nosql/`** - Contains all NoSQL-related functionality.

Each folder includes a `main.py` file along with supporting functional modules for CRUD operations, aggregation, joins, selection, filtering, and more.

## Execution
To run commands, navigate to the respective folder and execute:
```bash
python3 main.py
```
This will launch a command-line interface where users can enter commands. Use `exit` to close the session.

## SQL Operations
### **Table Creation**
```sql
CREATE TABLE newTable (id, name, val);
```
- Creates CSV-based tables.
- If the table does not exist, generates a new CSV file with the specified attributes.

### **Data Manipulation**
```sql
INSERT INTO newTable (401, 'Jake Doe', 100000);
UPDATE INTO newTable <uuid> (id 999, val 420);
DELETE FROM newTable <uuid>;
```
- Supports inserting, updating, and deleting records from CSV tables.

### **Query Operations**
```sql
SELECT Title, rank, Country FROM YoutubeChannels WHERE rank > 1 GROUP BY Country ORDER BY Country;
FILTER [Youtuber, subscribers, rank] FROM YoutubeChannels WHERE rank >= 5;
JOIN ['Youtuber'], ['video_views_rank', 'country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fk WHERE country_rank >= 5 ORDER BY Youtuber;
```
- Includes filtering, projections, joins, aggregations, and ordering.

## NoSQL Operations
### **Table Creation**
```nosql
CREATE TABLE ZZ;
```
- Creates JSON-based tables.

### **Data Manipulation**
```nosql
INSERT INTO ZZ ( {"id":"1", "value":"Test"} );
UPDATE INTO ZZ <uuid> ( {"id":"99", "value":"updated"} );
DELETE FROM ZZ <uuid>;
```
- Supports inserting, updating, and deleting JSON records.

### **Query Operations**
```nosql
FILTER [Activity_Period, Operating_Airline, GEO_Region] FROM airline WHERE GEO_Region = 'US';
JOIN ['Activity_Period', 'GEO_Region'], ['Landing_Count'] FROM airline.uuid = details.fk WHERE Landing_Count == 1020;
SELECT Activity_Period, GEO_Summary, GEO_Region FROM airline WHERE GEO_Region == 'Caribbean' ORDER BY Activity_Period;
```
- Includes filtering, selections, joins, and aggregations.

## License
This project is open-source and available under the [MIT License](LICENSE).
