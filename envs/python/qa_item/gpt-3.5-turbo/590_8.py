from urllib.parse import urlparse

def parse_http_request_line(response: str) -> dict:
    # Split the response string by spaces to get method, url, and version
    parts = response.split(" ")
    
    if len(parts) < 3:
        return None
    
    method = parts[0]
    url = parts[1]
    http_version = parts[2]
    
    # Parse the URL to get the path and query parameters
    parsed_url = urlparse(url)
    path = parsed_url.path
    query_params = parsed_url.query
    
    return {
        "method": method,
        "url": url,
        "http_version": http_version,
        "path": path,
        "query_params": query_params
    }
import unittest


class Tester(unittest.TestCase):

    def test_valid_post_request_line(self):
        response = "POST /api/data HTTP/1.1\r\n"
        parsed_info = parse_http_request_line(response)
        self.assertEqual(parsed_info["method"], "POST")
        self.assertEqual(parsed_info["url"], "/api/data")
        self.assertEqual(parsed_info["http_version"], "HTTP/1.1")

    def test_put_request_line(self):
        response = "PUT /api/update HTTP/2.0\r\n"
        parsed_info = parse_http_request_line(response)
        self.assertEqual(parsed_info["method"], "PUT")
        self.assertEqual(parsed_info["url"], "/api/update")
        self.assertEqual(parsed_info["http_version"], "HTTP/2.0")

    def test_delete_request_line(self):
        response = "DELETE /api/delete HTTP/1.1\r\n"
        parsed_info = parse_http_request_line(response)
        self.assertEqual(parsed_info["method"], "DELETE")
        self.assertEqual(parsed_info["url"], "/api/delete")
        self.assertEqual(parsed_info["http_version"], "HTTP/1.1")

    def test_malformed_request_line(self):
        response = "INVALID REQUEST LINE\r\n"
        parsed_info = parse_http_request_line(response)
        self.assertEqual(parsed_info, {})  # Expect empty result for malformed request
if __name__ == '__main__':
    unittest.main()