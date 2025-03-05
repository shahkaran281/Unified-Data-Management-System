import sys
import re
import uuid
import os
import csv
import json


def aggregate_table_2(tableName, count_attribute, attribute_list):
    distinct_counts = {}
    try:
        with open(f"data/{tableName}.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            file_headers = reader.fieldnames

            if count_attribute not in file_headers:
                print(
                    f"Error: Count attribute '{count_attribute}' not found in the file '{tableName}.csv'")
                return

            for attribute in attribute_list:
                if (attribute not in file_headers):
                    print(
                        f"Error: Attribute '{attribute}' not found in the file '{tableName}.csv'")
                    return

            for row in reader:
                count_value = row[count_attribute]
                if count_value in distinct_counts:
                    distinct_counts[count_value] += 1
                else:
                    distinct_counts[count_value] = 1

            for value, count in distinct_counts.items():
                print(f" {value},  {count}")

    except FileNotFoundError:
        print(
            f"Error: File '{tableName}.csv' not found in the 'data' directory.")


def aggregate_table(tableName, count_attribute, group_by, order_by=None, chunk_size=100):
    print(tableName, count_attribute, group_by, order_by)
    distinct_counts = {}
    chunk = []
    try:
        with open(f"data/{tableName}.json", 'r', newline='') as file:
            data = json.load(file)
        for curr_json in data:
            for key, value in curr_json.items():
                chunk.append(value)
                group_by_val = value.get(group_by, None)
                if (group_by_val is not None and group_by_val not in distinct_counts):
                    distinct_counts[group_by_val] = [
                        value.get(count_attribute, None)]
                elif (group_by_val is not None and group_by_val in distinct_counts):
                    distinct_counts[group_by_val].append(
                        value.get(count_attribute, None))
                if (len(chunk) == chunk_size):
                    process_chunk(distinct_counts)
                    chunk = []

        if (len(chunk) > 0):
            process_chunk(distinct_counts, isLastChunk=True, order_by=order_by)
        else:
            process_chunk(distinct_counts, isLastChunk=True, order_by=order_by)
            chunk = []
    except FileNotFoundError:
        print(
            f"Error: File '{tableName}.json' not found in the 'data' directory.")


def process_chunk(dict, isLastChunk=False, order_by=None):
    if (isLastChunk):
        unique_values_dict = {name: len(set(values))
                              for name, values in dict.items()}
        if (order_by):
            unique_values_dict = {k: v for k, v in sorted(
                unique_values_dict.items(), key=lambda item: item[1])}
        print(unique_values_dict)
    else:
        pass


if __name__ == "__main__":
    command = sys.argv[1]
    pattern = r'COUNT\(([^)]+)\)\s+,\s+(.+?)\s+FROM\s+(\w+)\s*GROUP BY\s+(\w+)\s*(?:ORDER BY\s+(\w+))?$'
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        count_attribute = match.group(1)
        attribute_list = match.group(2).split(',')
        stripped_attribute_list = [attribute.strip()
                                   for attribute in attribute_list]
        table = match.group(3)
        group_by = match.group(4)
        order_by = match.group(5)
        if (order_by):
            print(order_by)

        aggregate_table(table, count_attribute, group_by, order_by)

    else:
        print("Input string does not match the expected format. USE : UPDATE INTO <TABLE_NAME> <UUID> (<VALUE_ATTRIBUTES_SEPARATED_BY_COMMA>)")
