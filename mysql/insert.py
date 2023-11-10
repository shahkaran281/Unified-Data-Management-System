import sys
import re
import uuid
import os
import csv


def insert_table(tableName, values):
    print("Insert table called")
    print("Table Name:", tableName)
    print("Value List:", values)
    path = f"data/{table_name}.csv"
    values.insert(0, uuid.uuid4())
    if os.path.exists(path) == False:
        raise FileExistsError("Table Does not Exist")
    with open(path, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(values)


if __name__ == "__main__":
    print("Insert Called")
    command = sys.argv[1]
    print("Command:", command)
    pattern = r'INTO (\w+) \(([^)]+)\)'

    match = re.search(pattern, command, re.IGNORECASE)

    if match:
        table_name = match.group(1)
        value_attributes = match.group(2).split(',')
        value_attributes = [attr.strip() for attr in value_attributes]
        insert_table(table_name, value_attributes)

    else:
        print("Input string does not match the expected format. USE : INSERT INTO <TABLE_NAME> (<VALUE_ATTRIBUTES_SEPARATED_BY_COMMA>)")