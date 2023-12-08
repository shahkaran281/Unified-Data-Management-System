## Structure

We have separated both the SQL and NoSQL part into separate folder name 'mysql' and 'nosql' respectively. Inside both the folder, there is a main.py file and other functional files such as CRUD, aggregate, join, select, filter.

main.py : 'main.py' is a script that takes user input commands, parses them for keywords, and executes corresponding Python scripts with extracted arguments using 'subprocess.run()'.

So, in order to run any command, first go into respective folder and run the following command.
Command : python3 main.py

Now, it will launch a command line, where user can enter the command. To close it, use 'exit'

## SQL-like :

1. CREATE :
   Command : CREATE TABLE newTable ( id, name, val )

   Creates CSV-based tables via create_table(table_name , attributes).​
   Checks for an existing CSV file with the table name; if absent, generates a new CSV file with specified attributes.​

2. INSERT :
   Command : INSERT INTO newTable (401, Jake Doe, 100000)​

   Inserts values into CSV-based tables.​
   Checks for the table's existence, raising an error if not found.​
   Appends values to the CSV file as a new row.

3. UPDATE :
   Command : UPDATE INTO newTable c0fe9c1b-9f2c-4799-8a13-fdf38ab0a7ea ( id 999 , val 420)​

   load_row_by_value(csv_file, column_name, target_value): Retrieves a CSV row based on a specified value in a column.​
   update_table(tableName, uuid_to_update, values): Updates a CSV table by locating a row with a matching UUID, modifying specified attributes, and appending the updated row back to the CSV file.

4. DELETE​ :
   Command: DELETE FROM newTable 19a4c0d3-a796-4a2b-b0f7-ce622c82ccdc

   Action: This command seeks to delete the record of the employee with the UUID '12345' from the 'employees' table.

5. AGGREGATE :
   Command: AGGREGATE COUNT(channel_type) , Title, rank , category FROM YoutubeChannels GROUP BY Title​

   Action: Aggregates data in the 'table_name' CSV file, counting occurrences of 'attribute_name' while grouping data by 'group_by_attribute'.​
   Functionality: Implements CSV operations for data aggregation and grouping, ensuring attribute and table existence, then displaying distinct counts.

6. FILTER :
   Command : Filter [ Youtuber,subscribers,rank] from YoutubeChannels where rank >= 5​

   Filters data from a CSV-based table based on specified conditions.​
   Checks table existence, raises error if not found.​
   Retrieves filtered data and columns as per the conditions from the CSV file.

7. JOIN :
   Command : Join ['Youtuber'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fk WHERE country_rank >= 5 ORDER BY Youtuber​

   Joins and prints selected columns from two CSV-based tables.​
   Validates table existence, raises error if not found.​
   Performs a join operation on provided columns and condition between the tables

8. SELECT :
   Command : SELECT Title, rank , Country FROM YoutubeChannels WHERE rank > '1' GROUP BY Country ORDER BY Country​

   Executes updates in a CSV table based on specified attributes and conditions.​
   Handles WHERE, GROUP BY, and ORDER BY clauses.​
   Validates the command format and structure.

9. PROJ :
   Command : Proj [uuid, rank, Youtuber ] FROM YoutubeChannels​

   Prints an entire CSV table.​
   Verifies table existence, raises error if not found.​
   Prints all rows and columns from the specified CSV table.​
   For NoSQL, this operation has been merged into proj.

## NoSQL-like :

1. CREATE :
   Command : CREATE TABLE ZZ​

   Creates JSON-based tables by defining create_table(table_name).​
   Checks if a JSON file with the table name exists; if not, creates an empty JSON array file.

2. INSERT :
   Command : INSERT INTO ZZ ({"id":"1" , "value" : "Test"})​

   Inserts values into JSON-based tables.​
   Validates the table's existence, raising an error if not found.​
   Adds new data in JSON format to the existing JSON file after validation.

3. UPDATE :
   Command : UPDATE INTO ZZ cd01bde4-30b3-4a43-960c-184642f39399 ({"id" : "99" , "value": "updated"}))  
   ​
   update_table(table_name, uuid_to_update, value): Updates a JSON table by replacing the data associated with the provided UUID.​
   Validates JSON input, checking table existence and UUID match before updating.

4. DELETE​ :
   Command: DELETE FROM ZZ cd01bde4-30b3-4a43-960c-184642f39399​

   This command is intended to remove the record associated with the UUID 'cd01bde4-30b3-4a43-960c-184642f39399​' from the 'zz' JSON-based table.

5. AGGREGATE :
   Command: AGGREGATE COUNT(Operating_Airline) , GEO_Region FROM airline GROUP BY GEO_Region ORDER BY GEO_Region

   Action: Manages JSON data aggregation, counting occurrences of 'attribute_name' in the 'table_name' JSON file. It groups data by 'group_by_attribute' and optionally orders by 'order_by_attribute'.​
   Functionality: Handles JSON file manipulations, parses JSON data, conducts aggregation and grouping, and offers optional ordering based on specified attributes.

6. FILTER :
   Command : Filter [Activity_Period, Operating_Airline, GEO_Region] from airline where GEO_Region = US​

   Filters data from a JSON-based table based on provided conditions.​
   Validates table existence, raises error if not found.​
   Retrieves filtered data based on conditions from the JSON file.

7. JOIN :
   Command :Join [‘Activity_Period’ , ‘GEO_Region’ ], [‘Landing_Count’] FROM airline.uuid = details.fk WHERE Landing_Count == 1020​

   Joins and prints selected columns from two JSON-based tables.​
   Validates file existence, raises error if not found.​
   Processes chunks of JSON data and performs a join based on provided columns and condition.

8. SELECT :
   Command : SELECT Activity_Period , GEO_Summary , GEO_Region FROM airline WHERE GEO_Region == "Caribbean" ORDER BY Activity_Period​

   Manages updates in a JSON-based table given certain attributes and conditions.​
   Processes WHERE, GROUP BY, and ORDER BY clauses.​
   Validates the input command format and its structure.​
   Retrieves, filters, and sorts data from the specified JSON file.

9. PROJ :
   This functionality has been merged into SELECT
