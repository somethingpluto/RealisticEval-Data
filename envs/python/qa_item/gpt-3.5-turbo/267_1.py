from typing import Tuple

def extract_sld_tld(fqdn: str) -> Tuple[str, str]:
    second_level_domain = ""
    top_level_domain = ""
    
    parts = fqdn.split(".")
    if len(parts) >= 2:
        second_level_domain = parts[-2]
        top_level_domain = parts[-1]
    
    return (second_level_domain, top_level_domain)
import unittest


class TestExtractSldTld(unittest.TestCase):
    def test_standard_fqdn(self):
        # Test a typical FQDN
        self.assertEqual(extract_sld_tld("www.example.com"), ("example", "com"))

    def test_standard_fqdn2(self):
        # Test a typical FQDN
        self.assertEqual(extract_sld_tld("www.example.xyz"), ("example", "xyz"))

    def test_fqdn_with_subdomains(self):
        # Test an FQDN with multiple subdomains
        self.assertEqual(extract_sld_tld("blog.subdomain.example.com"), ("example", "com"))

    def test_numeric_tld(self):
        # Test a numeric TLD, which can occur in private networks
        self.assertEqual(extract_sld_tld("server.example.123"), ("example", "123"))

if __name__ == '__main__':
    unittest.main()