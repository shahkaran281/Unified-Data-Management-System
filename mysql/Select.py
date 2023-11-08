import sys
import re
import uuid
import os
import csv
import json




def select_table(tableName  , attribute_list , condition = None , group_by = None , order_by = None):
    selected_attributes = [] 
    

    # file_headers = None
    try:
        with open(f"data/{tableName}.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            file_headers = reader.fieldnames

            for attribute in attribute_list:
                if(attribute not in file_headers):
                    print(f"Error: Attribute '{attribute}' not found in the file '{tableName}.csv'")            
                    return
            
            for row in reader:
                selected_data = {attr: row[attr] for attr in attribute_list}
                selected_attributes.append(selected_data)
        
        # Apply condition to filter    
        
        if(condition):
            paramaters = condition.split(' ')
            paramater_list = [param.strip() for param in paramaters]
            if paramater_list[0] not in file_headers:
               print(f"Error: Attribute '{paramater_list[0]}' not found in the file '{tableName}.csv' for Filtering try with correct filter")
               return 
            filtered_data = [row for row in selected_attributes if eval(f"row['{paramater_list[0]}'] {paramater_list[1]} {paramater_list[2]}")]
            selected_attributes = filtered_data
        # if(group_by):      Think through this implementation
        #     print(group_by)
        if(order_by):
            if order_by not in file_headers:
                print(f"Order By Attribute {order_by} does not exist")
                return
            sorted_data = sorted(selected_attributes , key = lambda x: x[order_by])
            selected_attributes = sorted_data

        print(json.dumps(selected_attributes , indent = 4))

            
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