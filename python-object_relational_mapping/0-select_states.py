#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
And order it using ascending order
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name from arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor to execute queries
        cursor = db.cursor()

        # Execute SQL query to select all states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows
        rows = cursor.fetchall()

        # Print each row
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to databse, {e}")
    finally:
        # Clean up
        if cursor:
            cursor.close()
        if db:
            db.close()
