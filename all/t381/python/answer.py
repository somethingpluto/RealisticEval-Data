def extract_email_details(email):
    """
    Extracts the username and mailbox suffix from an email address.

    :param email: str, the email address to extract details from
    :return: tuple, (username, domain) where:
        username is the part before '@'
        domain is the part after '@'

    Example:
        extract_email_details("xxx@gmail.com") returns ('xxx', 'gmail.com')
    """
    # Check if '@' is in the email
    if '@' not in email:
        raise ValueError("Invalid email address. Email must contain an '@' character.")

    # Split the email at the '@' and assign parts to username and domain
    username, domain = email.split('@', 1)

    return username, domain