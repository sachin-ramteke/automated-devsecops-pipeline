from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleApp(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy", "security": "passed"}).encode())
        else:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": "DevSecOps Secure Web Service v1.0"}).encode())

def run():
    server = HTTPServer(('0.0.0.0', 8000), SimpleApp)
    print("Serving on port 8000...")
    server.serve_forever()

if __name__ == "__main__":
    run()
