def parse_http_request_line(response: str) -> dict:
    """
    Parses the first line of an HTTP request.

    Args:
        response (str): The raw HTTP request string.

    Returns:
        dict: A dictionary containing the method, URL, and HTTP version.
    """
    # Split the first line of the HTTP request
    first_line = response.splitlines()[0]
    
    # Split the first line into components
    parts = first_line.split()
    
    # Ensure the first line has the correct number of components
    if len(parts) != 3:
        raise ValueError("Invalid HTTP request line")
    
    # Extract method, URL, and HTTP version
    method, url, http_version = parts
    
    # Return the parsed components in a dictionary
    return {
        "method": method,
        "url": url,
        "http_version": http_version
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