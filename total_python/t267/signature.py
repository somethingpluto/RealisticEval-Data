from typing import Tuple


def extract_sld_tld(fqdn: str) -> Tuple[str, str]:
    """
    extract the second-level and top-level domain names from the fully qualified domain name FQDN and return them
    Args:
        fqdn (str): The fully qualified domain name.

    Returns:
        A tuple containing the second-level domain and top-level domain.
    """
