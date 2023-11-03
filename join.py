import re
import sys
import csv


def join_and_print_selected_columns(file1, file2, key1='uuid', key2='fk', columns1=[], columns2=[]):
    # Create dictionaries to store the data from each CSV file
    data1 = {}
    data2 = {}

    try:
        # Read the first file using 'key1' as the key
        with open(f'data/{file1}.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
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

    # Perform the join and print selected columns from both tables
    for key in data1:
        if key in data2:
            combined_data = {**data1[key], **data2[key]}
            selected_data1 = [combined_data.get(
                column, '') for column in columns1]
            selected_data2 = [combined_data.get(
                column, '') for column in columns2]
            print(", ".join(selected_data1) + ", " + ", ".join(selected_data2))


if __name__ == '__main__':
    # Your input string
    command = sys.argv[1]
    # "['Youtuber'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fk"
    pattern = r'\[(.*?)\],\s*\[(.*?)\]\s+FROM\s+(\S+)\s*\.(\S+)\s*=\s*(\S+)\s*\.(\S+)'
    match = re.match(pattern, command, re.IGNORECASE)

    if match:
        columns1_str = match.group(1).strip()
        columns2_str = match.group(2).strip()
        table1 = match.group(3)
        col1 = match.group(4)
        table2 = match.group(5)
        col2 = match.group(6)

        # Split the comma-separated strings into lists
        columns1 = [col.strip('\'').strip() for col in columns1_str.split(',')]
        columns2 = [col.strip('\'').strip() for col in columns2_str.split(',')]

        # Call the join_and_print_selected_columns function
        join_and_print_selected_columns(
            table1, table2, col1, col2, columns1, columns2)
    else:
        print(
            "No match found in the input string. PLEASE USE: JOIN [COLUMNS_FROM_TABLE1_SEPARATED_BY_COMMA], [COLUMNS_FROM_TABLE2_SEPARATED_BY_COMMA] FROM TABLE1.COL1 = TABLE2.COL2")
