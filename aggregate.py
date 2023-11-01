import sys
import re
import uuid
import os
import csv


def aggregate_table(tableName , count_attribute , attribute_list):
    distinct_counts = {} 
    try:
        with open(f"data/{tableName}.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            file_headers = reader.fieldnames

            if count_attribute not in file_headers:
                print(f"Error: Count attribute '{count_attribute}' not found in the file '{tableName}.csv'")
                return
            
            for attribute in attribute_list:
                if(attribute not in file_headers):
                    print(f"Error: Attribute '{attribute}' not found in the file '{tableName}.csv'")
                    return

            for row in reader:       
                count_value = row[count_attribute]                     
                if count_value in distinct_counts:
                    distinct_counts[count_value] += 1
                else:
                    distinct_counts[count_value] = 1
            
            for value , count in distinct_counts.items():
                print(f" {value},  {count}")

    except FileNotFoundError:
        print( f"Error: File '{tableName}.csv' not found in the 'data' directory.")




if __name__ == "__main__":
    command = sys.argv[1]
    pattern = r'COUNT\(([^)]+)\)\s+,\s+(.+?)\s+FROM\s+(\w+)(\s+GROUP BY\s+(\w+))?'
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        count_attribute = match.group(1)
        attribute_list = match.group(2).split(',')
        stripped_attribute_list = [attribute.strip() for attribute in attribute_list]
        table = match.group(3)
        group_by = match.group(4)
        if(group_by):
            print(group_by)
        print(count_attribute , attribute_list , table)
        aggregate_table(table, count_attribute, stripped_attribute_list)

    else:
        print("Input string does not match the expected format. USE : UPDATE INTO <TABLE_NAME> <UUID> (<VALUE_ATTRIBUTES_SEPARATED_BY_COMMA>)")