import sys
import re
import uuid
import os
import csv
import json

def print_pretty(data):
    if not data:
        print("No data to display.")
        return
    headers = list(data[0].keys())
    col_widths = [max(len(str(row[header])) for row in data + [dict(zip(headers, headers))]) for header in headers]
    header_line = '|'.join(f'{header:{width}}' for header, width in zip(headers, col_widths))
    separator_line = '+'.join('-' * (width + 2) for width in col_widths)
    print(separator_line)
    print(f'|{header_line}|')
    print(separator_line)
    for row in data:
        row_line = '|'.join(f'{row[header]:{width}}' for header, width in zip(headers, col_widths))
        print(f'|{row_line}|')
    print(separator_line)



def select_table(tableName  , attribute_list , condition = None , group_by = None , order_by = None , chunk_size = 2):
    try:
        with open(f"data/{tableName}.csv", 'r') as file:
            reader = csv.DictReader(file)
            file_headers = reader.fieldnames
            selected_attributes = []
            chunk = []

            for row in reader:
                selected_data = {attr: row[attr] for attr in attribute_list}
                chunk.append(selected_data)
                if len(chunk) == chunk_size:
                    if condition:
                        if condition.split()[0] not in file_headers:
                            print(f"Error: Attribute '{condition.split()[0]}' not found in the file '{tableName}.csv' for Filtering try with correct filter")
                            return
                        chunk = [r for r in chunk if eval(f"r['{condition.split()[0]}'] {condition.split()[1]} {condition.split()[2]}")]
                        selected_attributes.extend(chunk)
                    else:
                        selected_attributes.extend(chunk)
                    chunk = []
            if condition and len(chunk) > 0:
                chunk = [r for r in chunk if eval(f"r['{condition.split()[0]}'] {condition.split()[1]} {condition.split()[2]}")]
                selected_attributes.extend(chunk)
            elif len(chunk) > 0:
                selected_attributes.extend(chunk)
                 


        if order_by:
            if order_by not in file_headers:
                print(f"Error: Order By Attribute '{order_by}' does not exist.")
                return
            selected_attributes.sort(key=lambda x: x[order_by])
        print_pretty(selected_attributes)

            
    except FileNotFoundError:
        print( f"Error: File '{tableName}.csv' not found in the 'data' directory.")







if __name__ == "__main__":
    command = sys.argv[1]
    # print(command)
    pattern = r'([a-zA-Z,\s]+)\s+FROM\s+(\w+)\s*(?:WHERE\s+(.+?))?\s*(?:GROUP BY\s+(\w+))?\s*(?:ORDER BY\s+(\w+))?$'
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        # count_attribute = match.group(1)
        attribute_list = match.group(1).split(',')
        stripped_attribute_list = [attribute.strip() for attribute in attribute_list]
        table = match.group(2)
        condition = match.group(3)
        group_by = match.group(4)
        order_by = match.group(5)
        if(group_by):
            print(group_by)
        if(condition):
            print(condition)
        if(order_by):
            print(order_by)
        # print(stripped_attribute_list , table , group_by)
        select_table(table , stripped_attribute_list , condition , group_by , order_by)

    else:
        print("Input string does not match the expected format. USE : UPDATE INTO <TABLE_NAME> <UUID> (<VALUE_ATTRIBUTES_SEPARATED_BY_COMMA>)")