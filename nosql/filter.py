import json
import re
import os
import sys


def filter_json_in_chunks(input_json_file, condition, columns, chunk_size=100):
    json_file_path = f'data/{input_json_file}.json'

    if not os.path.exists(json_file_path):
        print("File not found:", json_file_path)
        return

    with open(json_file_path, 'r') as infile:
        # Load JSON data
        data = json.load(infile)

        if columns == 'all':
            print("All columns:")

            for item in data:
                key = next(iter(item))  # Extracting the UUID key
                row = item[key]  # Extracting the inner dictionary
                if not condition or evaluate_condition(row, condition):
                    if 'uuid' in columns:
                        print(key)
                    print(row)
        else:
            print("Selected columns:")
            print(columns)

            for i in range(0, len(data), chunk_size):
                chunk = data[i:i + chunk_size]

                for item in chunk:
                    key = next(iter(item))  # Extracting the UUID key
                    row = item[key]  # Extracting the inner dictionary
                    if not condition or evaluate_condition(row, condition):
                        if 'uuid' in columns:
                            print(key)
                        if columns == 'all':
                            print(row)
                        else:
                            selected_values = [row[col]
                                               for col in columns if col in row]
                            print(selected_values)


def evaluate_condition(row, condition):
    if not condition:
        return True

    condition_parts = re.match(
        r'(\w+\s*\w+\s*\w+)\s*([<>=!]+)\s*(\w+)', condition)
    if not condition_parts:
        print("Invalid condition format")
        return False

    column_name = condition_parts.group(1)
    operator = condition_parts.group(2)
    value = condition_parts.group(3)

    if column_name not in row:
        print("Column not found in row:", column_name)
        return False

    cell_value = row[column_name]

    try:
        # Ensure the values are represented as strings for string comparison
        cell_value_str = str(cell_value)
        value_str = str(value)

        # Perform string-based comparisons for supported operators
        if operator == '=':
            return cell_value_str == value_str
        elif operator == '>':
            return cell_value_str > value_str
        elif operator == '<':
            return cell_value_str < value_str
        elif operator == '>=':
            return cell_value_str >= value_str
        elif operator == '<=':
            return cell_value_str <= value_str
        elif operator == '!=':
            return cell_value_str != value_str
        else:
            print("Invalid operator in condition")
            return False

    except Exception as e:
        print("Error in condition evaluation:", e)
        return False


# Example usage:
if __name__ == "__main__":
    command = sys.argv[1]
    pattern = r"(?:all\s+from\s+(\w+))(?:\s+where\s+(.+))?|\[([^\]]+)\]\s+from\s+(\w+)(?:\s+where\s+(.+))?"

    match = re.match(pattern, command, re.IGNORECASE)

    if match:
        if match.group(1):
            table_name = match.group(1)
            condition = match.group(2) if match.group(2) else ""
            print("Condition:", condition)
            filter_json_in_chunks(table_name, condition, 'all')
        elif match.group(3):
            columns = [col.strip() for col in match.group(3).split(',')]
            table_name = match.group(4)
            condition = match.group(5) if match.group(5) else ""
            filter_json_in_chunks(table_name, condition, columns)
    else:
        print("Invalid expression")
