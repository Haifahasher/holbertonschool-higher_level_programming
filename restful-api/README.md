# RESTful API Project

This project contains several tasks focused on building and consuming RESTful APIs using Python. Each task builds upon the previous one, covering different aspects of API development.

## Tasks Overview

### Task 0: Basics of HTTP/HTTPS (Theoretical)
**Objective**: Understand the differences between HTTP and HTTPS, HTTP structure, methods, and status codes.

**Key Concepts**:
- **HTTP vs HTTPS**: HTTP is unencrypted, HTTPS adds SSL/TLS encryption for security
- **HTTP Methods**: GET, POST, PUT, DELETE, PATCH
- **HTTP Status Codes**: 1xx (Informational), 2xx (Success), 3xx (Redirection), 4xx (Client Errors), 5xx (Server Errors)

**Common HTTP Methods**:
- **GET**: Retrieve data (e.g., fetching a web page)
- **POST**: Submit data (e.g., creating a new user)
- **PUT**: Update entire resource (e.g., replacing user data)
- **DELETE**: Remove resource (e.g., deleting a user)
- **PATCH**: Partial update (e.g., updating specific user fields)

**Common HTTP Status Codes**:
- **200 OK**: Request successful
- **201 Created**: Resource created successfully
- **400 Bad Request**: Invalid request syntax
- **401 Unauthorized**: Authentication required
- **403 Forbidden**: Access denied
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

### Task 1: Consume data from an API using command line tools (curl)
**Objective**: Learn to use curl for API interactions.

**Key Commands**:
```bash
# Check curl version
curl --version

# Basic GET request
curl https://jsonplaceholder.typicode.com/posts

# Get only headers
curl -I https://jsonplaceholder.typicode.com/posts

# POST request with data
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

### Task 2: Consuming and processing data from an API using Python
**Objective**: Use Python requests library to fetch API data and process it.

**Files**:
- `task_02_requests.py`: Main implementation
- `main_02_requests.py`: Test script

**Functions**:
- `fetch_and_print_posts()`: Fetches posts and prints titles
- `fetch_and_save_posts()`: Fetches posts and saves to CSV

**Usage**:
```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python3 main_02_requests.py
```

### Task 3: Develop a simple API using Python with the `http.server` module
**Objective**: Build a basic HTTP server using Python's standard library.

**File**: `task_03_http_server.py`

**Endpoints**:
- `/`: Returns "Hello, this is a simple API!"
- `/data`: Returns JSON data `{"name": "John", "age": 30, "city": "New York"}`
- `/status`: Returns "OK"
- Any other endpoint: Returns 404 "Endpoint not found"

**Usage**:
```bash
python3 task_03_http_server.py
# Server runs on http://localhost:8000
```

**Testing with curl**:
```bash
curl http://localhost:8000/
curl http://localhost:8000/data
curl http://localhost:8000/status
curl http://localhost:8000/nonexistent
```

### Task 4: Develop a Simple API using Python with Flask
**Objective**: Build a more sophisticated API using Flask framework.

**File**: `task_04_flask.py`

**Endpoints**:
- `/`: Welcome message
- `/data`: List of all usernames
- `/status`: API status
- `/users/<username>`: Get user data by username
- `/add_user`: POST endpoint to add new users

**Usage**:
```bash
# Install Flask
pip install Flask

# Run the server
python3 task_04_flask.py
# Or use Flask CLI
flask --app task_04_flask.py run
```

**Testing with curl**:
```bash
# GET requests
curl http://localhost:5000/
curl http://localhost:5000/data
curl http://localhost:5000/status
curl http://localhost:5000/users/jane

# POST request
curl -X POST -H "Content-Type: application/json" \
  -d '{"username":"alice","name":"Alice","age":25,"city":"San Francisco"}' \
  http://localhost:5000/add_user
```

### Task 5: API Security and Authentication Techniques
**Objective**: Implement authentication and authorization in Flask API.

**File**: `task_05_basic_security.py`

**Features**:
- Basic HTTP Authentication
- JWT Token-based Authentication
- Role-based Access Control (admin/user roles)

**Endpoints**:
- `/basic-protected`: Basic auth protected route
- `/login`: JWT login endpoint
- `/jwt-protected`: JWT protected route
- `/admin-only`: Admin-only route

**Usage**:
```bash
# Install all dependencies
pip install -r requirements.txt

# Run the server
python3 task_05_basic_security.py
```

**Testing Authentication**:

1. **Basic Authentication**:
```bash
# Without credentials (should fail)
curl http://localhost:5000/basic-protected

# With credentials
curl -u user1:password http://localhost:5000/basic-protected
```

2. **JWT Authentication**:
```bash
# Login to get token
curl -X POST -H "Content-Type: application/json" \
  -d '{"username":"user1","password":"password"}' \
  http://localhost:5000/login

# Use token for protected routes
curl -H "Authorization: Bearer <YOUR_TOKEN>" \
  http://localhost:5000/jwt-protected

# Admin route (requires admin role)
curl -H "Authorization: Bearer <ADMIN_TOKEN>" \
  http://localhost:5000/admin-only
```

## Installation and Setup

1. **Clone the repository**:
```bash
git clone <repository-url>
cd restful-api
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run individual tasks**:
```bash
# Task 2: API consumption
python3 main_02_requests.py

# Task 3: HTTP server
python3 task_03_http_server.py

# Task 4: Flask API
python3 task_04_flask.py

# Task 5: Secure API
python3 task_05_basic_security.py
```

## Project Structure

```
restful-api/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── task_02_requests.py      # API consumption with requests
├── main_02_requests.py      # Test script for task 2
├── task_03_http_server.py   # Basic HTTP server
├── task_04_flask.py         # Flask API
└── task_05_basic_security.py # Secure API with authentication
```

## Key Learning Outcomes

- Understanding HTTP/HTTPS protocols and structure
- Using curl for API testing and debugging
- Building APIs with Python standard library and Flask
- Implementing authentication and authorization
- Handling different HTTP methods and status codes
- Processing JSON data and converting to other formats
- Error handling and proper HTTP response codes

## Security Notes

- The JWT secret key in Task 5 should be changed in production
- Passwords are hashed using Werkzeug's security functions
- All authentication errors return proper 401 status codes
- CORS headers are included for browser compatibility

## Testing

Each task includes examples and can be tested using:
- **curl**: Command-line HTTP client
- **Web browsers**: For GET requests
- **Python scripts**: For programmatic testing
- **Postman/Insomnia**: For comprehensive API testing

## Resources

- [MDN HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Requests Library](https://requests.readthedocs.io/)
- [JWT Introduction](https://jwt.io/introduction)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
