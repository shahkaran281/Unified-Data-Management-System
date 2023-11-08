import sys
import re
import uuid
import os
import json

# INSERT INTO EMPLOYEE ( { "id": "1" , "name" : "2" } )

def insert_table(tableName, values):
    print("Insert table called")
    print("Table Name:", tableName)
    print("Value List:", values)
    path = f"data/{table_name}.json"
    # values.insert(0 , uuid.uuid4())
    if os.path.exists(path) == False:
        raise FileExistsError("Table Does not Exist")
    with open(path, 'r') as file:
        json_array = json.load(file)
    
    # Handle the exception here for erorr in values to the JSON
    try:
        data = json.loads(values)
    except ValueError as e:
        raise (f"The input payload is wrong" , e)
    new_data = { str(uuid.uuid4()) : data } 
   
    # print(new_data)
    json_array.append(new_data)
    # print(json_array)
    with open(path, 'w') as file:
        json.dump(json_array, file, indent=4)

    



if __name__ == "__main__":
    print("Insert Called")
    command = sys.argv[1]
    print("Command:", command)
    pattern = r'INTO\s+(\w+)\s+\(([^)]+)\)'

    match = re.search(pattern, command, re.IGNORECASE)

    if match:
        table_name = match.group(1)
        value_attributes = match.group(2)
        insert_table(table_name, value_attributes)

    else:
        print("Input string does not match the expected format. USE : INSERT INTO <TABLE_NAME> (<VALUE_ATTRIBUTES_SEPARATED_BY_COMMA>)")
