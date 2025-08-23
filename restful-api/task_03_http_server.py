#!/usr/bin/env python3
"""
Task 3: Develop a simple API using Python with the http.server module
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Simple HTTP request handler for basic API endpoints
    """
    
    def do_GET(self):
        """
        Handle GET requests for different endpoints
        """
        if self.path == '/':
            # Root endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = "Hello, this is a simple API!"
            self.wfile.write(response.encode('utf-8'))
            
        elif self.path == '/data':
            # Data endpoint - return JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {"name": "John", "age": 30, "city": "New York"}
            response = json.dumps(data)
            self.wfile.write(response.encode('utf-8'))
            
        elif self.path == '/status':
            # Status endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            response = "OK"
            self.wfile.write(response.encode('utf-8'))
            
        else:
            # Undefined endpoint - return 404
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            response = "Endpoint not found"
            self.wfile.write(response.encode('utf-8'))
    
    def do_OPTIONS(self):
        """
        Handle preflight OPTIONS requests for CORS
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()


def run_server(port=8000):
    """
    Start the HTTP server
    """
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on port {port}")
    print(f"Visit http://localhost:{port} to test the API")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()


if __name__ == "__main__":
    run_server()
