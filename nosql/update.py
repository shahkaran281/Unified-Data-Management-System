import sys
import re
import os
import json



def update_table(table_name , uuid_to_update , value):
    print("Update table called")
    print("Table Name:", table_name)
    print("Value List:", value)
    print("UUID:" , uuid_to_update)
    path = f"data/{table_name}.json"
    # values.insert(0 , uuid.uuid4())
    if os.path.exists(path) == False:
        raise FileExistsError("Table Does not Exist")
    with open(path, 'r') as file:
        json_array = json.load(file)
        # Handle the exception here for erorr in values to the JSON
    try:
        data = json.loads(value)
    except ValueError as e:
        raise (f"The input payload is wrong" , e)
    print(data)
    found = any(uuid_to_update in item for item in json_array)
    if not found:
        raise ValueError(f"UUID '{uuid_to_update}' not found in the JSON data.")

    updated_json_array = [] 
    for item in json_array:
        if uuid_to_update in item:
            item[uuid_to_update] = data
        updated_json_array.append(item)
    with open(path, 'w') as file:
        json.dump(updated_json_array, file, indent=4)
    # print(updated_json_array)








if __name__ == "__main__":
    # print("Update Called")
    command = sys.argv[1]
    # print("Command:", command)
    pattern = r'INTO\s+(.+)\s+(.+)\s+\(([^)]+)\)'
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        table_name = match.group(1)
        uuid = match.group(2)
        value_attributes = match.group(3)
        # print(value_attributes)
        update_table(table_name, uuid, value_attributes)

    else:
        print("Input string does not match the expected format. USE : UPDATE INTO <TABLE_NAME> <UUID> (<VALUE_ATTRIBUTES_SEPARATED_BY_COMMA>)")