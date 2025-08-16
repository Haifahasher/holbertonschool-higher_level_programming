#!/usr/bin/env python3
"""
CSV to JSON Conversion Module

This module provides functionality to convert CSV data to JSON format
using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and save it to data.json.

    Args:
        csv_filename (str): The filename of the input CSV file

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read CSV data using DictReader
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Convert each row to a dictionary and collect in a list
            data = []
            for row in csv_reader:
                data.append(row)

        # Serialize the list of dictionaries to JSON
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except csv.Error as e:
        print(f"Error reading CSV file '{csv_filename}': {e}")
        return False
    except json.JSONEncodeError as e:
        print(f"Error encoding data to JSON: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
