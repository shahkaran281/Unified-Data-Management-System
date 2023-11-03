# Filter [  Youtuber,subscribers] from YoutubeChannels where rank >= 5
# Filter all from YoutubeChannels where rank >= 5
import csv
import re
import os
import sys


def filter_csv_to_list(input_csv_file, condition, columns):
    csv_file_path = f'data/{input_csv_file}.csv'

    if not os.path.exists(csv_file_path):
        print("File not found:", csv_file_path)
        return

    # Track if "Column not found" message has been printed
    column_not_found_message_printed = False

    with open(csv_file_path, 'r', newline='') as infile:
        reader = csv.reader(infile)

        # Read and store the header row
        header = next(reader)

        if columns != 'all':
            missing_columns = [
                column_name for column_name in columns if column_name not in header]
            if missing_columns:
                column_not_found_message_printed = True
                print("Column from list not found in Table:",
                      ", ".join(missing_columns))
                return

        if columns == 'all':
            print(" ".join(header))
        else:
            print(" ".join(columns))  # Print selected columns with spaces

        for row in reader:
            # Pass the column_not_found_message_printed flag to evaluate_condition
            if evaluate_condition(row, condition, header, column_not_found_message_printed):
                if columns == 'all':
                    print(" ".join(row))  # Print the entire row with spaces
                else:
                    selected_values = [
                        row[header.index(column_name)] for column_name in columns]
                    # Print selected values with spaces
                    print(" ".join(selected_values))


def evaluate_condition(row, condition, header, column_not_found_message_printed):
    # Implement your custom condition evaluation logic here
    # Condition format: 'column_name operator value'
    condition_parts = re.match(r'(\w+)\s*([<>=]+)\s*(\d+)', condition)
    if not condition_parts:
        print("Invalid condition format")
        return False

    column_name = condition_parts.group(1)
    operator = condition_parts.group(2)
    value = float(condition_parts.group(3))

    if column_name not in header:
        # Check if the error message has been printed, and print it only once
        if not column_not_found_message_printed:
            print("Column not found in condition:", column_name)
        # Set the flag to indicate that the message has been printed
        column_not_found_message_printed = True
        return False

    # Find the column index in the header
    column_index = header.index(column_name)
    # Convert value to the appropriate data type (e.g., float)
    value = float(value)

    try:
        # Convert cell value to the same type
        cell_value = float(row[column_index])
    except ValueError:
        print(f"Invalid data in column {column_name}")
        return False

    if operator == '<':
        return cell_value < value
    elif operator == '>':
        return cell_value > value
    elif operator == '=':
        return cell_value == value
    elif operator == '<=':
        return cell_value <= value
    elif operator == '>=':
        return cell_value >= value
    else:
        print("Invalid operator in condition")
        return False


# Example usage:
if __name__ == "__main__":

    # command = "[  Youtuber,subscribers] from YoutubeChannels where rank >= 5"
    command = sys.argv[1]
    pattern = r"(?:all\s+from\s+(\w+)\s+where\s+(.+))|\[([^\]]+)\]\s+from\s+(\w+)\s+where\s+(.+)"

    match = re.match(pattern, command, re.IGNORECASE)

    if match:
        if match.group(1):
            table_name = match.group(1)
            condition = match.group(2)
            # Initialize the flag
            column_not_found_message_printed = False
            # Call filter_csv_to_list with 'all' type
            filter_csv_to_list(table_name, condition, 'all')
        elif match.group(3):
            columns = [col.strip() for col in match.group(3).split(',')]
            table_name = match.group(4)
            condition = match.group(5)
            # print("Type: selected")
            # print("Columns:", columns)
            # print("Table Name:", table_name)
            # print("Condition:", condition)
            # Initialize the flag
            column_not_found_message_printed = False
            filter_csv_to_list(table_name, condition, columns)

    else:
        print("Invalid expression")
