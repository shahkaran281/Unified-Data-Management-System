import sys
import re


def delete_table(tableName, uuid):
    print("Delete table called")
    print("TableName:", tableName)
    print("UUID:", uuid)


if __name__ == "__main__":
    print("Delete Called")
    command = sys.argv[1]
    print("Command:", command)
    pattern = r'^from ([A-Za-z][A-Za-z0-9]*) ([A-Za-z0-9]+)'
    match = re.search(pattern, command, re.IGNORECASE)

    if match:
        table_name = match.group(1)
        uuid = match.group(2)
        delete_table(table_name, uuid)
    else:
        print("Input string does not match the expected format.USE: DELETE FROM <TABLE_NAME> <UUID>")
