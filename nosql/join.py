import json
import re
import sys


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

        if order_by:
            if order_by not in selected_data[0]:
                print(f"Order By Attribute '{order_by}' does not exist")
                return []
            selected_data = sorted(selected_data, key=lambda x: x[order_by])

        return selected_data

    columns = columns1 + columns2

    # Chunking the data
    for i in range(0, len(data1), chunk_size):
        for j in range(0, len(data2), chunk_size):
            chunk1 = data1[i:i + chunk_size]
            chunk2 = data2[j:j + chunk_size]

            selected_data = process_chunk(chunk1, chunk2)
            # Print the headers and values for each chunk
            if selected_data:
                for item in selected_data:
                    print('\t'.join([str(item.get(column, 'None'))
                          for column in columns]))
    # values = list(item.values())
    # print("\t".join(map(str, values)))
    # print()


if __name__ == '__main__':
    command = sys.argv[1]
    # command = "['name', 'age'], ['job', 'city'] FROM Table1.uuid = Table2.fk Where age > 25"

    pattern = r'\[(.+?)\],\s*\[(.+?)\]\s+FROM\s+(\S+)\.(\S+)\s*=\s*(\S+)\.(\S+)\s*(?:WHERE\s+(.+?))?\s*(?:ORDER BY\s+(\w+))?$'
    match = re.match(pattern, command, re.IGNORECASE)

    if match:
        columns1_str = match.group(1).strip()

        columns2_str = match.group(2).strip()
        table1 = match.group(3)
        col1 = match.group(4)
        table2 = match.group(5)
        col2 = match.group(6)
        where = match.group(7)
        order = match.group(8)
        columns1 = list(re.findall(r"‘(.*?)’", columns1_str))
        columns2 = list(re.findall(r"‘(.*?)’", columns2_str))

        join_and_print_selected_columns(
            table1, table2, col1, col2, columns1, columns2, condition=where, order_by=order)
    else:
        print("No match found in the input string.")
