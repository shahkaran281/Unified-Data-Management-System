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
    idx+=1
    bash_script = f"sed '{idx}d' data/{tableName}.csv | tee data/{tableName}.csv"
    print(bash_script)
    # Need to update the values
    for val in values:
        current_param_val = val.split(' ')
        param = current_param_val[0]
        new_value = current_param_val[1]
        result[param] = new_value
    subprocess.run(bash_script , shell=True , check=True)
    

    print(result)

    # Check if the result is a dictionary (indicating a valid row) or an error message
    # if isinstance(result, dict):
    #     print("Row found:", result)
    # else:
    #     print("Error:", result)


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
