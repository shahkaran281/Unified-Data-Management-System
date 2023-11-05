import re
import sys
import csv
import json


def join_and_print_selected_columns(file1, file2, key1='uuid', key2='fk', columns1=[], columns2=[], condition=None, group_by=None, order_by=None):
    # Create dictionaries to store the data from each CSV file
    data1 = {}
    data2 = {}

    try:
        # Read the first file using 'key1' as the key
        with open(f'data/{file1}.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            file_headers1 = reader.fieldnames

            for row in reader:
                if key1 in row:
                    data1[row[key1]] = row
                else:
                    print(f"Key '{key1}' not found in table '{file1}'.")
                    return
    except FileNotFoundError:
        print(f"Table '{file1}' not found.")
        return

    try:
        # Read the second file using 'key2' as the key
        with open(f'data/{file2}.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if key2 in row:
                    data2[row[key2]] = row
                else:
                    print(f"Key '{key2}' not found in table '{file2}'.")
                    return
    except FileNotFoundError:
        print(f"Table '{file2}' not found.")
        return

    # Remove single quotes from column names
    columns1 = [col.strip('\'') for col in columns1]
    columns2 = [col.strip('\'') for col in columns2]

    # Check if all columns from input exist in the data
    missing_columns1 = [
        col for col in columns1 if col not in data1.get(next(iter(data1), {}))]
    missing_columns2 = [
        col for col in columns2 if col not in data2.get(next(iter(data2), {}))]

    if missing_columns1:
        print(
            f"Columns {', '.join(missing_columns1)} not found in table {file1}.")
        return
    if missing_columns2:
        print(
            f"Columns {', '.join(missing_columns2)} not found in table {file2}.")
        return
    # print(json.dumps(data1, indent=4))

    # print(json.dumps(data2, indent=4))
    # Perform the join and print selected columns from both tables
    # for key in data1:
    #     if key in data2:
    #         combined_data = {**data1[key], **data2[key]}
    #         selected_data1 = [combined_data.get(
    #             column, '') for column in columns1]
    #         selected_data2 = [combined_data.get(
    #             column, '') for column in columns2]
    #         print(", ".join(selected_data1) + ", " + ", ".join(selected_data2))
    selected_data = []
    for key in data1:
        if key in data2:
            combined_data = {**data1[key], **data2[key]}
            selected_data1 = {column: combined_data.get(
                column, '') for column in columns1}
            selected_data2 = {column: combined_data.get(
                column, '') for column in columns2}
            combined_selected_data = {**selected_data1, **selected_data2}
            selected_data.append(combined_selected_data)
    headers = list(selected_data[0].keys())
    if condition:
        paramaters = condition.split(' ')
        parameter_list = [param.strip() for param in paramaters]
        if parameter_list[0] not in headers:
            print(
                f"Error: Attribute '{parameter_list[0]}' not found. For filtering, try with correct filter")
            return
        selected_data = [row for row in selected_data if eval(
            f"str(row['{parameter_list[0]}']) {parameter_list[1]} str(parameter_list[2])")]
    # print(json.dumps(selected_data, indent=4))
    if (order_by):
        if order_by not in headers:
            print(f"Order By Attribute {order_by} does not exist")
            return
        sorted_data = sorted(selected_data, key=lambda x: x[order_by])
        selected_data = sorted_data
    # print(selected_data)
    # Print the headers only once
    headers = list(selected_data[0].keys())
    print("\t".join(headers))

    # Print the values line by line
    for item in selected_data:
        values = list(item.values())
        print("\t".join(values))
    # for row in selected_data:
    #     print(row)
    # print(headers)


if __name__ == '__main__':
    # Your input string
    command = sys.argv[1]
    # command = "['Youtuber'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fk WHERE country_rank >= 5 ORDER BY Youtuber"
    # "x"
    pattern = r'\[(.+?)\],\s*\[(.+?)\]\s+FROM\s+(\S+)\s*\.(\S+)\s*=\s*(\S+)\s*\.(\S+)\s*(?:WHERE\s+(.+?))?\s*(?:GROUP BY\s+(\w+))?\s*(?:ORDER BY\s+(\w+))?$'
    match = re.match(pattern, command, re.IGNORECASE)

    if match:
        columns1_str = match.group(1).strip()
        columns2_str = match.group(2).strip()
        table1 = match.group(3)
        col1 = match.group(4)
        table2 = match.group(5)
        col2 = match.group(6)
        where = match.group(7)
        group = match.group(8)
        order = match.group(9)

        # if where:
        #     print("Where:", where)
        # if group:
        #     print("group:", group)
        # if order:
        #     print("order:", order)
        # Split the comma-separated strings into lists
        columns1 = [col.strip('\'').strip() for col in columns1_str.split(',')]
        columns2 = [col.strip('\'').strip() for col in columns2_str.split(',')]

        # Call the join_and_print_selected_columns function
        join_and_print_selected_columns(
            table1, table2, col1, col2, columns1, columns2, condition=where, order_by=order)
    else:
        print(
            "No match found in the input string. PLEASE USE: JOIN [COLUMNS_FROM_TABLE1_SEPARATED_BY_COMMA], [COLUMNS_FROM_TABLE2_SEPARATED_BY_COMMA] FROM TABLE1.COL1 = TABLE2.COL2")
