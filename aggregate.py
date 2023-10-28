import sys
import re
import uuid
import os
import csv


def aggregate_table(tableName , count_attribute , attribute_list):
    # print(tableName , count_attribute , attribute_list)    
    all_distinct = set()
    try:
        with open(f"data/{tableName}.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                all_distinct.add(row[count_attribute])
        print(len(all_distinct))
    except Exception as e:
        return str(e)  # Return the error message if an exception occurs




if __name__ == "__main__":
    # print("Aggregate Called")
    command = sys.argv[1]
    # print("Command:", command)
    pattern = r'COUNT\(([^)]+)\) , (.+?) FROM (\w+)'
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        count_attribute = match.group(1)
        attribute_list = match.group(2).split(', ')
        table = match.group(3)
        print(count_attribute , attribute_list , table)
        # print(value_attributes)
        aggregate_table(table, count_attribute, attribute_list)

    else:
        print("Input string does not match the expected format. USE : UPDATE INTO <TABLE_NAME> <UUID> (<VALUE_ATTRIBUTES_SEPARATED_BY_COMMA>)")