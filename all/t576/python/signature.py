def hide_bank_account(account: str) -> str:
    """
    Hides the sensitive part of a bank account number with 17 digits, showing only the last 4 characters.

    For example:
        - Input: 12345678901234567
        - Output: ****4567

    Args:
        account (str): The bank account number to hide. This must be exactly 17 characters long.

    Returns:
        str: The bank account number with the first part hidden, formatted as "****XXXX",
             where "XXXX" are the last four digits of the account.

    Raises:
        ValueError: If the account number is not exactly 17 characters long.
    """