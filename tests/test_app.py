import unittest
import threading
import time
import urllib.request
import json
from app.main import SimpleApp
from http.server import HTTPServer

class TestSimpleApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(('127.0.0.1', 8085), SimpleApp)
        cls.thread = threading.Thread(target=cls.server.serve_forever)
        cls.thread.daemon = True
        cls.thread.start()
        time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_root_endpoint(self):
        req = urllib.request.Request("http://127.0.0.1:8085/")
        with urllib.request.urlopen(req) as response:
            self.assertEqual(response.status, 200)
            data = json.loads(response.read().decode())
            self.assertIn("DevSecOps Secure Web Service", data["message"])

    def test_health_endpoint(self):
        req = urllib.request.Request("http://127.0.0.1:8085/health")
        with urllib.request.urlopen(req) as response:
            self.assertEqual(response.status, 200)
            data = json.loads(response.read().decode())
            self.assertEqual(data["status"], "healthy")
            self.assertEqual(data["security"], "passed")

if __name__ == "__main__":
    unittest.main()
