#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
This version is safe from MySQL injections.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    
    # Create cursor
    cursor = db.cursor()
    
    # Execute query using parameterized query (safe from SQL injection)
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Display results
    for row in results:
        print(row)
    
    # Close connections
    cursor.close()
    db.close()
