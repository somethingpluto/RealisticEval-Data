
from typing import Tuple

def extract_sld_tld(fqdn: str) -> Tuple[str, str]:
    """
    extract the second-level and top-level domain names from the fully qualified domain name FQDN and return them
    Args:
        fqdn (str): The fully qualified domain name.

    Returns:
        A tuple containing the second-level domain and top-level domain.
    """
    # Iterate through all the subdomains of the fqdn
    subdomains: List[str] = []
    for subdomain in fqdn.split("."):
        # Split the subdomain into its component parts
        subdomain_parts = subdomain.split(".", 1)
        # Add the subdomain to the list of subdomains
        subdomains.append(subdomain_parts[0])
        # Split the subdomain_parts[1] into its component parts
        subdomain_parts_2 = subdomain_parts[1].split(".", 1)
        # Add the subdomain_parts_2 to the list of subdomains
        subdomains.append(subdomain_parts_2[0])
        # Split the subdomain_parts_2 into its component parts
        subdomain_parts_3 = subdomain_parts_2[1].split(".", 1)
        # Add the subdomain_parts_3 to the list of subdomains
        subdomains.append(subdomain_parts_3[0])
    
    # Iterate through the list of subdomains
    for subdomain in subdomains:
        # Extract the second-level domain and top-level domain
        sld = subdomain[0]
        tld = subdomain[1]
        
        # Return the tuple with the second-level domain and top-level domain
        return (sld, tld)

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