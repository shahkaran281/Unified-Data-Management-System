import re
import sys
import csv

def join_and_print_selected_columns(file1, file2, key1='uuid', key2='fk', columns1=[], columns2=[]):
    # Create dictionaries to store the data from each CSV file
    data1 = {}
    data2 = {}

    # Read the first file using 'key1' as the key
    with open(file1, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data1[row[key1]] = row

    # Read the second file using 'key2' as the key
    with open(file2, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data2[row[key2]] = row

    # Remove single quotes from column names
    columns1 = [col.strip('\'') for col in columns1]
    columns2 = [col.strip('\'') for col in columns2]

    # Perform the join and print selected columns from both tables
    for key in data1:
        if key in data2:
            combined_data = {**data1[key], **data2[key]}
            selected_data1 = [combined_data[column] for column in columns1]
            selected_data2 = [combined_data[column] for column in columns2]
            print(", ".join(selected_data1) + ", " + ", ".join(selected_data2))

if __name__ == '__main__':
    # Your input string
    command = sys.argv[1]
    # "['Youtuber'], ['video_views_rank','country_rank'] FROM YoutubeChannels.uuid = YoutubeViews.fk"

    # Define a regex pattern with the re.IGNORECASE flag
    pattern = r'\[(.*?)\], \[(.*?)\] FROM (.+?)\.(.+) = (.+?)\.(.+)'

    # Match the pattern with re.IGNORECASE
    match = re.match(pattern, command, re.IGNORECASE)

    if match:
        # Extract the values
        columns1_str = match.group(1)
        columns2_str = match.group(2)
        table1 = match.group(3)
        col1 = match.group(4)
        table2 = match.group(5)
        col2 = match.group(6)

        # Split the comma-separated strings into lists
        columns1 = [col.strip('\'') for col in columns1_str.split(',')]
        columns2 = [col.strip('\'') for col in columns2_str.split(',')]

        # print("columns1:", columns1)
        # print("columns2:", columns2)
        # print("table1:", table1)
        # print("col1:", col1)
        # print("table2:", table2)
        # print("col2:", col2)

        # Call the join_and_print_selected_columns function
        join_and_print_selected_columns(f'data/{table1}.csv', f'data/{table2}.csv', col1, col2, columns1, columns2)
    else:
        print("No match found in the input string.")
