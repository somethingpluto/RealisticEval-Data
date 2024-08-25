import unittest


class TestExtractSldTld(unittest.TestCase):
    def test_standard_fqdn(self):
        # Test a typical FQDN
        self.assertEqual(extract_sld_tld("www.example.com"), ("example", "com"))

    def test_fqdn_with_subdomains(self):
        # Test an FQDN with multiple subdomains
        self.assertEqual(extract_sld_tld("blog.subdomain.example.com"), ("example", "com"))

    def test_single_level_domain(self):
        # Test a domain that is missing a TLD or SLD
        with self.assertRaises(ValueError):
            extract_sld_tld("localhost")

    def test_edge_case_empty_string(self):
        # Test with an empty string
        with self.assertRaises(ValueError):
            extract_sld_tld("")

    def test_numeric_tld(self):
        # Test a numeric TLD, which can occur in private networks
        self.assertEqual(extract_sld_tld("server.example.123"), ("example", "123"))