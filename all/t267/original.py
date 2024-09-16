def extract_2ld(fqdn):
    """Generated with ChatGPT.

    Extract the second level domain from a fully qualified domain name (FQDN).
    :param fqdn: Fully qualified domain name
    :return: 2LD and TLD combined
    """

    if not fqdn:
        raise ValueError("FQDN is empty")

    # First try with tldextract
    extracted = tldextract.extract(fqdn)
    if extracted.domain and extracted.suffix:
        # If both parts are identified, return them
        return f"{extracted.domain}.{extracted.suffix}"

    # Fallback mechanism
    parts = fqdn.split('.')

    # Basic assumption: The last two parts are the domain and TLD
    if len(parts) >= 2:
        return f"{parts[-2]}.{parts[-1]}"

    # Return the original
    return fqdn
