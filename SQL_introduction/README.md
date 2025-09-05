# SQL Introduction

This directory contains SQL scripts for learning MySQL database operations.

## Files

- `0-list_databases.sql` - Lists all databases
- `1-create_database_if_missing.sql` - Creates database hbtn_0c_0
- `2-remove_database.sql` - Deletes database hbtn_0c_0
- `3-list_tables.sql` - Lists all tables in a database
- `4-first_table.sql` - Creates first_table with id and name columns
- `5-full_table.sql` - Shows full table description
- `6-list_values.sql` - Lists all rows in first_table
- `7-insert_value.sql` - Inserts a new row with id=89, name='Best School'
- `8-count_89.sql` - Counts records with id=89
- `9-full_creation.sql` - Creates second_table with multiple rows
- `10-top_score.sql` - Lists records ordered by score (descending)
- `11-best_score.sql` - Lists records with score >= 10
- `12-no_cheating.sql` - Updates Bob's score to 10
- `13-change_class.sql` - Removes records with score <= 5
- `14-average.sql` - Computes average score
- `15-groups.sql` - Counts records by score
- `16-no_link.sql` - Lists records excluding NULL names

## Usage

Each script can be executed using MySQL command line:

```bash
cat script_name.sql | mysql -hlocalhost -uroot -p database_name
```

## Requirements

- MySQL 8.0
- Ubuntu 22.04 LTS
- All SQL keywords in uppercase
- Comments before each query
- Files end with newline
