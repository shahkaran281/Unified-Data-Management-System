import sys
import re
import uuid
import os
import json




def select_table(tableName  , attribute_list , condition = None , group_by = None , order_by = None , chunk_size = 2):
    try:
        selected_attributes = []
        chunk = []
        # print(tableName , attribute_list , condition ,group_by , order_by )
        with open(f"data/{tableName}.json", 'r') as file:
            data = json.load(file)

        if(group_by):
            if(group_by not in attribute_list):
                raise "f Group by attribute {group_by} is not present"
        if(order_by):
            if(order_by not in attribute_list):
                raise "f Order by attribute {order_by} is not present" 
        
        for curr_json in data:
            for key , value in curr_json.items():
                selected_data = {attr: value.get(attr , None) for attr in attribute_list}
                chunk.append(selected_data)        
                if(len(chunk) == chunk_size):
                    if condition:
                        chunk = [r for r in chunk if r.get(condition.split()[0]) is not None and eval(f"r['{condition.split()[0]}'] {condition.split()[1]} {condition.split()[2]}")]
                        selected_attributes.extend(chunk)
                    else:
                        selected_attributes.extend(chunk)
                    chunk = []
        if condition and len(chunk) > 0:
            chunk = [r for r in chunk if r.get(condition.split()[0]) is not None and eval(f"r['{condition.split()[0]}'] {condition.split()[1]} {condition.split()[2]}")]
            selected_attributes.extend(chunk)
        elif len(chunk) > 0:
            selected_attributes.extend(chunk)
        if(order_by):
            selected_attributes.sort(key=lambda x: x[order_by])
        print(selected_attributes)

    except FileNotFoundError:
        print( f"Error: File '{tableName}.csv' not found in the 'data' directory.")

    



if __name__ == "__main__":
    command = sys.argv[1]
    # print(command)
    pattern = r'([a-zA-Z_,\s]+)\s+FROM\s+(\w+)\s*(?:WHERE\s+(.+?))?\s*(?:GROUP BY\s+(\w+))?\s*(?:ORDER BY\s+(\w+))?$'
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        # count_attribute = match.group(1)
        attribute_list = match.group(1).split(',')
        stripped_attribute_list = [attribute.strip() for attribute in attribute_list]
        table = match.group(2)
        condition = match.group(3)
        group_by = match.group(4)
        order_by = match.group(5)
        # if(group_by):
        #     print(group_by)
        # if(condition):
        #     print(condition)
        # if(order_by):
        #     print(order_by)
        
        select_table(table , stripped_attribute_list , condition , group_by , order_by)

    else:
        print("Input string does not match the expected format. USE : UPDATE INTO <TABLE_NAME> <UUID> (<VALUE_ATTRIBUTES_SEPARATED_BY_COMMA>)")