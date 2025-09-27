# Python Server-Side Rendering

This project demonstrates server-side rendering (SSR) using Python and Flask, leveraging the Jinja templating engine to create dynamic, efficient, and SEO-friendly web applications.

## Learning Objectives

- Understand the concepts of server-side rendering and how it differs from client-side rendering
- Learn the benefits of using server-side rendering in web development
- Implement SSR in Python using the Flask framework
- Utilize Jinja templating engine to dynamically generate HTML pages
- Read and display data from various sources including JSON, CSV, and SQLite databases
- Handle dynamic content and user inputs in web applications

## Project Structure

```
python-server_side_rendering/
├── task_00_intro.py          # Simple templating program
├── task_01_jinja.py          # Basic HTML template in Flask
├── task_02_logic.py          # Dynamic template with loops and conditions
├── task_03_files.py          # Display data from JSON/CSV files
├── task_04_db.py             # Extend to include SQLite
├── setup_database.py         # Database setup script
├── templates/                # Jinja HTML templates
│   ├── header.html
│   ├── footer.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── items.html
│   └── product_display.html
├── items.json               # Sample items data
├── products.json            # Products data in JSON format
├── products.csv             # Products data in CSV format
└── README.md
```

## Tasks

### Task 0: Creating a Simple Templating Program
- **File**: `task_00_intro.py`
- **Purpose**: Generate personalized invitation files from a template with placeholders
- **Features**:
  - String templating with placeholders
  - File operations for reading templates and writing output files
  - Error handling for various edge cases
  - Input validation and type checking

### Task 1: Creating a Basic HTML Template in Flask
- **File**: `task_01_jinja.py`
- **Purpose**: Basic Flask application with Jinja templates
- **Features**:
  - Simple Flask application setup
  - HTML templates with reusable components
  - Navigation between pages
  - Header and footer templates

### Task 2: Creating a Dynamic Template with Loops and Conditions
- **File**: `task_02_logic.py`
- **Purpose**: Dynamic content rendering with Jinja loops and conditions
- **Features**:
  - JSON data reading
  - Jinja loops and conditional statements
  - Dynamic list rendering
  - Empty state handling

### Task 3: Displaying Data from JSON or CSV Files
- **File**: `task_03_files.py`
- **Purpose**: Display product data from multiple file formats
- **Features**:
  - JSON and CSV file reading
  - Query parameter handling
  - Product filtering by ID
  - Error handling for invalid inputs

### Task 4: Extending Dynamic Data Display to Include SQLite
- **File**: `task_04_db.py`
- **Purpose**: Extend functionality to include SQLite database
- **Features**:
  - SQLite database integration
  - Multiple data source support (JSON, CSV, SQL)
  - Database error handling
  - Consistent template rendering

## Setup and Installation

1. **Install Flask**:
   ```bash
   pip install Flask
   ```

2. **Set up the database** (for Task 4):
   ```bash
   python setup_database.py
   ```

3. **Run the applications**:
   ```bash
   # Task 1: Basic Flask app
   python task_01_jinja.py
   
   # Task 2: Dynamic templates
   python task_02_logic.py
   
   # Task 3: JSON/CSV data
   python task_03_files.py
   
   # Task 4: SQLite integration
   python task_04_db.py
   ```

## Usage Examples

### Task 0: Simple Templating
```python
from task_00_intro import generate_invitations

template = "Hello {name}, you are invited to {event_title}..."
attendees = [{"name": "Alice", "event_title": "Conference", ...}]
generate_invitations(template, attendees)
```

### Task 1-4: Flask Applications
- Navigate to `http://localhost:5000` for the home page
- Visit `/about` and `/contact` for additional pages
- For Task 2: Visit `/items` to see dynamic content
- For Tasks 3-4: Visit `/products?source=json`, `/products?source=csv`, or `/products?source=sql`
- Add `&id=1` to filter by product ID

## Key Features

- **Server-Side Rendering**: HTML pages generated on the server
- **Jinja Templating**: Dynamic content rendering with loops and conditions
- **Multiple Data Sources**: JSON, CSV, and SQLite database support
- **Error Handling**: Comprehensive error handling for edge cases
- **Reusable Components**: Header and footer templates for consistency
- **Query Parameters**: URL-based filtering and data source selection

## Technologies Used

- **Python 3.x**: Core programming language
- **Flask**: Web framework for Python
- **Jinja2**: Templating engine for dynamic HTML generation
- **SQLite**: Lightweight database for data storage
- **JSON/CSV**: Data interchange formats

## Benefits of Server-Side Rendering

1. **SEO Friendly**: Search engines can easily crawl and index content
2. **Performance**: Faster initial page loads
3. **Accessibility**: Works without JavaScript enabled
4. **Security**: Sensitive logic stays on the server
5. **Maintainability**: Clear separation of concerns

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
- [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)
