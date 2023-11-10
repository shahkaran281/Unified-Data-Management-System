import re
import sys
import csv

def print_csv_table(table_name):
    try:
        with open(f'data/{table_name}.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                formatted_row = ' '.join(row)
                print(formatted_row)
    except FileNotFoundError:
        print(f"Table '{table_name}' not found.")

def print_selected_columns(table_name, columns_to_print):
    try:
        with open(f'data/{table_name}.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
            if not columns_to_print:
                # If columns_to_print is empty, print all columns
                columns_to_print = fieldnames
            else:
                # Check if the specified columns are valid
                for col in columns_to_print:
                    if col not in fieldnames:
                        print(f"Column '{col}' not found in the table.")
                        return

            # Print column headings
            print(', '.join(columns_to_print))

            for row in reader:
                formatted_row = [row[col] for col in columns_to_print]
                print(', '.join(formatted_row))
    except FileNotFoundError:
        print(f"Table '{table_name}' not found.")

if __name__ == "__main__":
    # Test the function with your 'command' query
    command = sys.argv[1]
    # print("Proj Called:",command)
    pattern1 = r'^all\s+FROM\s+(\w+)$'
    # Example : Proj all FROM YoutubeChannels
    pattern2 = r'^\[(.*?)\]\s+FROM\s+(\w+)$'
    # Example : Proj [Youtuber,rank] FROM YoutubeChannels

    # Try to match the query with both patterns
    match1 = re.match(pattern1, command , re.IGNORECASE)
    match2 = re.match(pattern2, command , re.IGNORECASE)

    if match1:
        table_name = match1.group(1)
        values = ['all']
        print_csv_table(table_name)
    elif match2:
        values_str = match2.group(1)
        table_name = match2.group(2)
        values = [val.strip() for val in values_str.split(',')]
        # print("Table:", table_name)
        # print("Values:",values)
        print_selected_columns(table_name,values)

    else:
        print("Error: Query doesn't match the expected patterns.PLEASE USE: PROJ ALL/[COL1,COL2,...] FROM TABLE")