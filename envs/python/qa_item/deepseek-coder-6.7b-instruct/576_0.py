def hide_bank_account(account: str) -> str:
    """
    Hides the sensitive part of a bank account number with 17 digits, showing only the last 4 characters.

    Args:
        account (str): The bank account number to hide. This must be exactly 17 characters long.

    Returns:
        str: The bank account number with the first part hidden, formatted as "****XXXX",
             where "XXXX" are the last four digits of the account.

    Raises:
        ValueError: If the account number is not exactly 17 characters long.
    """
    if len(account) != 17:
        raise ValueError("The account number must be exactly 17 characters long.")
    
    return f"****{account[-4:]}"
import unittest


class TestHideBankAccount(unittest.TestCase):
    def test_should_return_hidden_part_for_valid_account(self):
        self.assertEqual(hide_bank_account('12345678901234567'), '****4567')

    def test_should_return_hidden_part_for_another_valid_account(self):
        self.assertEqual(hide_bank_account('98765432109876543'), '****6543')

    def test_should_return_hidden_part_for_yet_another_valid_account(self):
        self.assertEqual(hide_bank_account('11111111111111100'), '****1100')

    def test_should_throw_error_for_shorter_account(self):
        with self.assertRaises(Exception):
            hide_bank_account('1234567890123456')

    def test_should_throw_error_for_longer_account(self):
        with self.assertRaises(Exception):
            hide_bank_account('123456789012345678')

    def test_should_throw_error_for_empty_account(self):
        with self.assertRaises(Exception):
            hide_bank_account('')

if __name__ == '__main__':
    unittest.main()