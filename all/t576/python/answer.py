def hide_bank_account(account: str) -> str:
    """
    Hides the sensitive part of a bank account number with 17 numbers, showing only the last 4 characters.

    :param account: The bank account number to hide.
    :return: The bank account number with the first part hidden.
    :raises ValueError: Raises an error if the account number is not exactly 17 characters long.
    """
    # Validate that the account number is exactly 17 characters long
    if len(account) != 17:
        raise ValueError("Account number must be exactly 17 characters long.")

    # Create the hidden representation with "****" prefix
    hidden_part = "****"

    # Extract the visible part of the account number (last 4 characters)
    visible_part = account[-4:]  # Get last 4 characters

    # Return the formatted string with hidden and visible parts
    return hidden_part + visible_part

