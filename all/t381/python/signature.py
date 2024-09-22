def extract_email_details(email: str):
    """
    Extracts the username and mailbox suffix from an email address.eg extract_email_details("xxx@gmail.com") returns ('xxx', 'gmail.com')
    Args:
        email (str): the email address to extract details from

    Returns:
        tuple: (username, domain)
    """
