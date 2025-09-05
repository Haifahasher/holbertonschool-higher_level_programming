# Python Object-Relational Mapping (ORM)

This directory contains Python scripts for Object-Relational Mapping using MySQLdb and SQLAlchemy to interact with MySQL databases.

## Files

### MySQLdb Scripts (Tasks 0-5)
- `0-select_states.py` - Lists all states from database using MySQLdb
- `1-filter_states.py` - Filters states starting with 'N' using MySQLdb
- `2-my_filter_states.py` - Filters states by user input (vulnerable to SQL injection)
- `3-my_safe_filter_states.py` - SQL injection safe filter using parameterized queries
- `4-cities_by_state.py` - Lists all cities with their states using JOIN
- `5-filter_cities.py` - Filters cities by state name

### SQLAlchemy Models and Scripts (Tasks 6-14)
- `model_state.py` - State class definition using SQLAlchemy
- `7-model_state_fetch_all.py` - Lists all State objects using SQLAlchemy
- `8-model_state_fetch_first.py` - Gets the first State object
- `9-model_state_filter_a.py` - Filters states containing letter 'a'
- `10-model_state_my_get.py` - Gets state by name
- `11-model_state_insert.py` - Adds new state "Louisiana"
- `12-model_state_update_id_2.py` - Updates state with id=2 to "New Mexico"
- `13-model_state_delete_a.py` - Deletes states containing letter 'a'
- `model_city.py` - City class definition with foreign key to State
- `14-model_city_fetch_by_state.py` - Lists all cities with their states

## Requirements

- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- MySQL 8.0 on Ubuntu 20.04 LTS
- All files must be executable
- All files must start with `#!/usr/bin/python3`
- All files must end with a newline
- Proper documentation for modules, classes, and functions
- Code must pass pycodestyle (version 2.7.*)

## Installation

### MySQLdb
```bash
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient==2.0.3
```

### SQLAlchemy
```bash
sudo pip3 install SQLAlchemy==1.4.22
```

## Usage

### MySQLdb Scripts
```bash
./script_name.py username password database_name [additional_args]
```

### SQLAlchemy Scripts
```bash
./script_name.py username password database_name [additional_args]
```

## Key Features

- **SQL Injection Protection**: Parameterized queries in safe scripts
- **Object-Relational Mapping**: SQLAlchemy models with proper relationships
- **Database Operations**: CRUD operations using both MySQLdb and SQLAlchemy
- **Foreign Key Relationships**: City model with reference to State
- **Proper Error Handling**: Safe database connections and session management

## Database Setup

Scripts work with various databases:
- `hbtn_0e_0_usa` - Basic states table
- `hbtn_0e_4_usa` - States and cities with relationships
- `hbtn_0e_6_usa` - States table for SQLAlchemy operations
- `hbtn_0e_14_usa` - States and cities for advanced ORM operations
