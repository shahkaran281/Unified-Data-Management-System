import sys
import re
import os
import json

def create_table(table_name):
    try:
        path = f"data/{table_name}.json"
        print(table_name)
        if os.path.exists(path):
            raise FileExistsError("Table Exists Already")
        with open(path , 'w' ) as file:
            file.write('[]')

    except FileExistsError as e:
        print(f"Error: {e}")




if __name__ == "__main__":
    command = sys.argv[1]
    pattern = r'TABLE\s+(\w+)$'

    match = re.search(pattern, command, re.IGNORECASE)

    if match:
        table_name = match.group(1)
        create_table(table_name)
    else:
        print("Invalid command format. Missing terms after TABLE")
