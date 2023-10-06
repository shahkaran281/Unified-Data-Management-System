import sys
import re


def update_table(tableName, uuid, values):
    print("Update Table function")
    print("Table Name:", tableName)
    print("UUID:", uuid)
    print("Values:", values)


if __name__ == "__main__":
    print("Update Called")
    command = sys.argv[1]
    print("Command:", command)
    pattern = r'INTO (\w+) (\w+) \(([^)]+)\)'
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        table_name = match.group(1)
        uuid = match.group(2)
        value_attributes = match.group(3).split(',')
        update_table(table_name, uuid, value_attributes)

    else:
        print("Input string does not match the expected format. USE : UPDATE INTO <TABLE_NAME> <UUID> (<VALUE_ATTRIBUTES_SEPARATED_BY_COMMA>)")
