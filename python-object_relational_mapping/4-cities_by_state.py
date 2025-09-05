#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
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
    
    # Execute query with JOIN to get cities and states
    cursor.execute("""
        SELECT cities.id, cities.name, states.name 
        FROM cities 
        JOIN states ON cities.state_id = states.id 
        ORDER BY cities.id ASC
    """)
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Display results
    for row in results:
        print(row)
    
    # Close connections
    cursor.close()
    db.close()
