def hide_bank_account(account: str) -> str:
    """
    Hides the sensitive part of a bank account number with 17 numbers, showing only the last 4 characters.

    For example:
        input: 12345678901234567
        output: ****4567

    :param account: The bank account number to hide.
    :return: The bank account number with the first part hidden.
    :raises ValueError: Raises an error if the account number is not exactly 17 characters long.
    """