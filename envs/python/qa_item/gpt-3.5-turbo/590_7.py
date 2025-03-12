from urllib.parse import urlparse

def parse_http_request_line(response: str) -> dict:
    lines = response.split('\r\n')
    method, url, version = lines[0].split(' ')
    
    parsed_url = urlparse(url)
    
    return {
        'method': method,
        'URL': url,
        'HTTP_version': version,
        'parsed_URL': {
            'scheme': parsed_url.scheme,
            'netloc': parsed_url.netloc,
            'path': parsed_url.path,
            'params': parsed_url.params,
            'query': parsed_url.query,
            'fragment': parsed_url.fragment
        }
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