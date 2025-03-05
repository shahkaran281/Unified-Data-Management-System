import re
import sys
import csv
import json


def merge_sort(arr, key):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half, key)
        merge_sort(right_half, key)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def merge_sort_json(data, key):
    if len(data) <= 1:
        return data
    # Splitting the JSON data into two halves
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    # Recursive call to sort each half
    left = merge_sort_json(left, key)
    right = merge_sort_json(right, key)
    return merge_json(left, right, key)


def merge_json(left, right, key):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx][key] < right[right_idx][key]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    # Adding remaining elements
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result


def merge_sort_custom_page(data, key, page_size):
    # Splitting the data into pages of specified size
    pages = [data[i:i + page_size] for i in range(0, len(data), page_size)]
    # Sort each page using merge sort
    for i, page in enumerate(pages):
        pages[i] = merge_sort_json(page, key)
    # Merge sorted pages
    while len(pages) > 1:
        merged_pages = []
        for i in range(0, len(pages), 2):
            if i + 1 < len(pages):
                merged = merge_json(pages[i], pages[i + 1], key)
                merged_pages.append(merged)
            else:
                merged_pages.append(pages[i])
        pages = merged_pages
    return pages[0] if pages else []


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
