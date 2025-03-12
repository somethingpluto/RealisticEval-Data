def hide_bank_account(account: str) -> str:
    if len(account) != 17:
        raise ValueError("The account number must be exactly 17 characters long.")
    return "****" + account[-4:]
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