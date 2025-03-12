def parse_http_request_line(response: str) -> dict:
    """
    Parses the first line of an HTTP request.

    Args:
        response (str): The raw HTTP request string.

    Returns:
        dict: A dictionary containing the method, URL, and HTTP version.
    """
    # Split the response into lines
    lines = response.split('\n')

    # The first line contains the request method, URL, and HTTP version
    request_line = lines[0].split(' ')

    # Return a dictionary with the method, URL, and HTTP version
    return {
        'method': request_line[0],
        'url': request_line[1],
        'http_version': request_line[2]
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