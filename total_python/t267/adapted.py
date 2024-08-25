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
