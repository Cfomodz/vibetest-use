#!/usr/bin/env python3
"""
Simple HTTP server to serve the test website for Vibetest demo
"""

import http.server
import socketserver
import os
import sys

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    print(f"🌐 Starting test website server on http://localhost:{PORT}")
    print(f"📁 Serving files from: {DIRECTORY}")
    print(f"📄 Test website: http://localhost:{PORT}/test_website.html")
    print("\nPress Ctrl+C to stop the server\n")
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped.")
            sys.exit(0)

if __name__ == "__main__":
    main()