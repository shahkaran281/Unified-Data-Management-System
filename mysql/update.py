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



def update_table(tableName, uuid_to_update, values):
    for i in range(len(values)):
        values[i] = values[i].strip()
    # print("Update Table function")
    # print("Table Name:", tableName)
    # print("UUID:", uuid_to_update)
    # print("Values:", values)
    
    # Load the items to update
    result , idx = load_row_by_value(f"data/{tableName}.csv", 'uuid', uuid_to_update)
    print(result , idx)
    process = subprocess.Popen([f"scripts/update.sh" , str(idx+2) , f"data/{tableName}.csv" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Print the verbose output
    print("Standard Output:")
    print(stdout.decode())  # Decode bytes to string for Python 3.x

    print("Standard Error:")
    print(stderr.decode())  # Decode bytes to string for Python 3.x
    
    for value in values:
        attribute = value.split(' ')[0]
        new_val = value.split(' ')[1]
        # print(attribute , new_val)
        result[attribute] = new_val
    print(result)

    with open(f"data/{tableName}.csv", 'a', newline='\n') as csvfile:
        fieldnames = result.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow(result)

    # Check if the CSV file is empty and write header if needed
    # if csvfile.tell() == 0:
    #     writer.writeheader()

    # Write the dictionary to the CSV file
    

# print(f"Data has been written to {csv_file_path}")







if __name__ == "__main__":
    # print("Update Called")
    command = sys.argv[1]
    # print("Command:", command)
    pattern = r'INTO (.+) (.+) \(([^)]+)\)'
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        table_name = match.group(1)
        uuid = match.group(2)
        value_attributes = match.group(3).split(',')
        # print(value_attributes)
        update_table(table_name, uuid, value_attributes)

    else:
        print("Input string does not match the expected format. USE : UPDATE INTO <TABLE_NAME> <UUID> (<VALUE_ATTRIBUTES_SEPARATED_BY_COMMA>)")
