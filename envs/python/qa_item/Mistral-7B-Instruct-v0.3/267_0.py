from dns.resolver import resolve
from typing import Tuple

def extract_sld_tld(fqdn: str) -> Tuple[str, str]:
    """
    extract the second-level and top-level domain names from the fully qualified domain name FQDN and return them
    Args:
        fqdn (str): The fully qualified domain name.

    Returns:
        A tuple containing the second-level domain and top-level domain.
    """
    try:
        response = resolve(fqdn, 'TXT')
        for rdata in response:
            if rdata.lower().startswith('v=spf1 ip4:'):
                domain_parts = rdata.split(';')[0].split('ip4:')[1].split(' ')
                sld = domain_parts[0]
                tld = domain_parts[-1]
                return sld, tld
    except Exception as e:
        print(f"Error: {e}")
        return '', ''
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