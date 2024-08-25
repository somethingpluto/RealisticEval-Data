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
def extract_sld_tld(fqdn):
    """
    Extracts the second-level domain (SLD) and top-level domain (TLD) from a fully qualified domain name (FQDN).

    Args:
    fqdn (str): The fully qualified domain name.

    Returns:
    tuple: A tuple containing the second-level domain and top-level domain.
    """
    # Split the FQDN into parts
    parts = fqdn.split('.')

    # Check if there are enough parts to extract SLD and TLD
    if len(parts) < 2:
        raise ValueError("The provided FQDN does not contain enough parts to extract SLD and TLD.")

    # Extract the SLD and TLD
    sld = parts[-2]  # Second to last item is the SLD
    tld = parts[-1]  # Last item is the TLD

    return sld, tld
