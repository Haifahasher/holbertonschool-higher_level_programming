# SQL More Queries

This directory contains SQL scripts for advanced MySQL database operations including user management, table constraints, and complex queries.

## Files

### User Management
- `0-privileges.sql` - Lists privileges of MySQL users user_0d_1 and user_0d_2
- `1-create_user.sql` - Creates user_0d_1 with all privileges
- `2-create_read_user.sql` - Creates user_0d_2 with SELECT privilege only

### Table Constraints
- `3-force_name.sql` - Creates table with NOT NULL name constraint
- `4-never_empty.sql` - Creates table with default id value
- `5-unique_id.sql` - Creates table with unique id constraint

### Database Structure
- `6-states.sql` - Creates states table with auto-increment primary key
- `7-cities.sql` - Creates cities table with foreign key to states

### Query Operations
- `8-cities_of_california_subquery.sql` - Lists California cities using subquery
- `9-cities_by_state_join.sql` - Lists cities with states using JOIN

### TV Shows Database Queries
- `10-genre_id_by_show.sql` - Lists shows with genres (INNER JOIN)
- `11-genre_id_all_shows.sql` - Lists all shows with genres (LEFT JOIN)
- `12-no_genre.sql` - Lists shows without genres
- `13-count_shows_by_genre.sql` - Counts shows by genre
- `14-my_genres.sql` - Lists genres for Dexter show
- `15-comedy_only.sql` - Lists Comedy shows only
- `16-shows_by_genre.sql` - Lists all shows and their genres

## Usage

Each script can be executed using MySQL command line:

```bash
cat script_name.sql | mysql -hlocalhost -uroot -p database_name
```

## Requirements

- MySQL 8.0
- Ubuntu 20.04 LTS
- All SQL keywords in uppercase
- Comments before each query
- Files end with newline
- Proper error handling with IF NOT EXISTS/IF EXISTS

## Database Setup

For TV shows queries (tasks 10-16), import the database dump:

```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```
