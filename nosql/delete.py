import sys
import re
import json
import subprocess
import os



def delete_table(tableName, uuid_to_del):
    print("Delete table called")
    print("TableName:", tableName)
    print("UUID:", uuid)
    path = f"data/{table_name}.json"

    if os.path.exists(path) == False:
        raise FileExistsError("Table Does not Exist")
    with open(path, 'r') as file:
        json_array = json.load(file)

    if any(uuid_to_del in item for item in json_array):
        updated_json_array = [item for item in json_array if uuid_to_del not in item]
    else:
        raise ValueError(f"UUID '{uuid_to_del}' not found in the JSON array.")
    
    with open(path, 'w') as file:
        json.dump(updated_json_array, file, indent=4)
    print(updated_json_array)


if __name__ == "__main__":
    print("Delete Called")
    command = sys.argv[1]
    print("Command:", command)
    pattern = r'^from ([A-Za-z][A-Za-z0-9]*) ([A-Za-z0-9-]+)'
    match = re.search(pattern, command, re.IGNORECASE)

    if match:
        table_name = match.group(1)
        uuid = match.group(2)
        delete_table(table_name, uuid)
    else:
        print("Input string does not match the expected format.USE: DELETE FROM <TABLE_NAME> <UUID>")