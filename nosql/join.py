import json
import re
import sys


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


def join_and_print_selected_columns(file1, file2, key1='uuid', key2='fk', columns1=[], columns2=[], condition=None, order_by=None, chunk_size=100):
    # Read JSON files
    try:
        with open(f'data/{file1}.json', 'r') as json_file:
            data1 = json.load(json_file)
    except FileNotFoundError:
        print(f"File '{file1}.json' not found.")
        return

    try:
        with open(f'data/{file2}.json', 'r') as json_file:
            data2 = json.load(json_file)
    except FileNotFoundError:
        print(f"File '{file2}.json' not found.")
        return

    # Function to process chunks of data
    def process_chunk(chunk1, chunk2):
        selected_data = []
        for item1 in chunk1:
<<<<<<< HEAD
            for item2 in chunk2:
                if item1[key1] == item2[key2]:
                    combined_data = {**item1, **item2}
                    selected_data.append(combined_data)

        if condition:
            # Implement condition filtering
            paramaters = condition.split(' ')
            parameter_list = [param.strip() for param in paramaters]
            if parameter_list[0] not in selected_data[0]:
                print(
                    f"Error: Attribute '{parameter_list[0]}' not found. For filtering, try with correct filter")
                return []
            selected_data = [row for row in selected_data if eval(
                f"str(row['{parameter_list[0]}']) {parameter_list[1]} str(parameter_list[2])")]
=======
            for key1, value1 in item1.items():
                for item2 in chunk2:
                    for key2, value2 in item2.items():
                        if key1 == value2.get("fk"):
                            combined_data = {**value1, **value2}
                            selected_data.append(combined_data)
        if condition:
            # print(f'Condition: {condition}')
            # Implement condition filtering
            # paramaters = condition.split(' ')
            # parameter_list = [param.strip() for param in paramaters]
            # if parameter_list[0] not in selected_data[0]:
            #     print(
            #         f"Error: Attribute '{parameter_list[0]}' not found. For filtering, try with correct filter")
            #     return []
            # selected_data = [row for row in selected_data if eval(
            #     f"str(row['{parameter_list[0]}']) {parameter_list[1]} str(parameter_list[2])")]
            selected_data = [r for r in selected_data if r.get(condition.split()[0]) is not None and eval(
                f"r['{condition.split()[0]}'] {condition.split()[1]} {condition.split()[2]}")]
>>>>>>> main

        if order_by:
            if order_by not in selected_data[0]:
                print(f"Order By Attribute '{order_by}' does not exist")
                return []
            selected_data = sorted(selected_data, key=lambda x: x[order_by])

        return selected_data

<<<<<<< HEAD
=======
    columns = columns1 + columns2

>>>>>>> main
    # Chunking the data
    for i in range(0, len(data1), chunk_size):
        for j in range(0, len(data2), chunk_size):
            chunk1 = data1[i:i + chunk_size]
            chunk2 = data2[j:j + chunk_size]

            selected_data = process_chunk(chunk1, chunk2)
<<<<<<< HEAD

            # Print the headers and values for each chunk
            if selected_data:
                headers = list(selected_data[0].keys())
                print("\t".join(headers))

                for item in selected_data:
                    values = list(item.values())
                    print("\t".join(map(str, values)))
=======
            # Print the headers and values for each chunk
            if selected_data:
                for item in selected_data:
                    print('\t'.join([str(item.get(column, 'None'))
                          for column in columns]))
    # values = list(item.values())
    # print("\t".join(map(str, values)))
    # print()
>>>>>>> main


if __name__ == '__main__':
    command = sys.argv[1]
    # command = "['name', 'age'], ['job', 'city'] FROM Table1.uuid = Table2.fk Where age > 25"

    pattern = r'\[(.+?)\],\s*\[(.+?)\]\s+FROM\s+(\S+)\.(\S+)\s*=\s*(\S+)\.(\S+)\s*(?:WHERE\s+(.+?))?\s*(?:ORDER BY\s+(\w+))?$'
    match = re.match(pattern, command, re.IGNORECASE)

    if match:
        columns1_str = match.group(1).strip()
<<<<<<< HEAD
=======

>>>>>>> main
        columns2_str = match.group(2).strip()
        table1 = match.group(3)
        col1 = match.group(4)
        table2 = match.group(5)
        col2 = match.group(6)
        where = match.group(7)
        order = match.group(8)
<<<<<<< HEAD

        columns1 = [col.strip('\'').strip() for col in columns1_str.split(',')]
        columns2 = [col.strip('\'').strip() for col in columns2_str.split(',')]
=======
        columns1 = list(re.findall(r"‘(.*?)’", columns1_str))
        columns2 = list(re.findall(r"‘(.*?)’", columns2_str))
>>>>>>> main

        join_and_print_selected_columns(
            table1, table2, col1, col2, columns1, columns2, condition=where, order_by=order)
    else:
        print("No match found in the input string.")
