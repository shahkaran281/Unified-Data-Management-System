import sys
import re


def create_table(table_name, attributes):
    # Implement the logic to create the table here
    # You should replace placeholders with actual values and create the table

    print(f"Creating table")
    print("TableName:", table_name)
    print("Attributes:", attributes)


if __name__ == "__main__":

    command = sys.argv[1]
    matchTable = re.match(r'TABLE (.+)', command, re.IGNORECASE)
    if matchTable:
        command_text = matchTable.group(1).strip()
        match = re.match(r'^(\w+)\s*\(([^)]+)\)$', command_text)
        if match:
            table_name = match.group(1)
            attributes = match.group(2).strip()
            attribute_list = [attr.strip() for attr in attributes.split(',')]
            create_table(table_name, attribute_list)
        else:
            print(
                "Invalid command format. Please use:CREATE TABLE <TABLE_NAME> (<ATTRIBUTES>)")
    else:
        print(
            "Invalid command format. Missing terms after TABLE")
