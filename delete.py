import sys
import re
import csv
import subprocess


# Function to load a specific row based on a known value in a column
def load_row_by_value(csv_file, column_name, target_value):
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for idx, row in enumerate(reader):
                if row[column_name] == target_value:
                    return row , idx 
            # If the loop completes without finding the target value, raise an exception
            raise ValueError(f"Target value '{target_value}' not found in column '{column_name}'.")
    except Exception as e:
        return str(e)  # Return the error message if an exception occurs

def delete_table(tableName, uuid_to_del):
    print("Delete table called")
    print("TableName:", tableName)
    print("UUID:", uuid)
    result , idx = load_row_by_value(f"data/{tableName}.csv", 'uuid', uuid_to_del)
    print(result , idx)
    process = subprocess.Popen([f"scripts/update.sh" , str(idx+2) , f"data/{tableName}.csv" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Print the verbose output
    print("Standard Output:")
    print(stdout.decode())  # Decode bytes to string for Python 3.x

    print("Standard Error:")
    print(stderr.decode())  # Decode bytes to string for Python 3.x


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
