#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file
"""
import sys
import os

# Import the required functions
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

# Get command line arguments (excluding the script name)
args = sys.argv[1:]

# Load existing list from file if it exists, otherwise start with empty list
filename = "add_item.json"
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add all arguments to the list
my_list.extend(args)

# Save the updated list back to the file
save_to_json_file(my_list, filename)
