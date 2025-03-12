from typing import List
from collections import defaultdict

def check_dividend_variances(records: List) -> List:
    dividends = defaultdict(list)

    for record in records:
        ticker, ex_dividend_date, dividend_amount = record
        dividends[ex_dividend_date].append(dividend_amount)

    variances = []
    for date, amounts in dividends.items():
        if len(set(amounts)) > 1:
            variances.append((ticker[0], ex_dividend_date) for ticker in dividends[date])

    return variances
import unittest


class TestCheckDividendVariances(unittest.TestCase):

    def test_no_inconsistencies(self):
        records = [
            ('AAPL', '2023-09-01', 0.22),
            ('AAPL', '2023-09-01', 0.22),
            ('MSFT', '2023-09-01', 0.56),
            ('GOOG', '2023-09-02', 0.00)
        ]
        expected_output = []
        self.assertEqual(check_dividend_variances(records), expected_output)

    def test_one_inconsistency(self):
        records = [
            ('AAPL', '2023-09-01', 0.22),
            ('AAPL', '2023-09-01', 0.23),  # Different amount
            ('MSFT', '2023-09-01', 0.56),
            ('GOOG', '2023-09-02', 0.00)
        ]
        expected_output = [('AAPL', '2023-09-01')]
        self.assertEqual(check_dividend_variances(records), expected_output)

    def test_multiple_inconsistencies(self):
        records = [
            ('AAPL', '2023-09-01', 0.22),
            ('AAPL', '2023-09-01', 0.23),  # Different amount
            ('MSFT', '2023-09-01', 0.56),
            ('MSFT', '2023-09-01', 0.60),  # Different amount
            ('GOOG', '2023-09-02', 0.00),
            ('TSLA', '2023-09-03', 0.10),
            ('TSLA', '2023-09-03', 0.10),  # Same amount, no inconsistency
            ('TSLA', '2023-09-03', 0.15)  # Different amount
        ]
        expected_output = [('AAPL', '2023-09-01'), ('MSFT', '2023-09-01'), ('TSLA', '2023-09-03')]
        self.assertEqual(check_dividend_variances(records), expected_output)

    def test_single_record(self):
        records = [
            ('AAPL', '2023-09-01', 0.22)
        ]
        expected_output = []
        self.assertEqual(check_dividend_variances(records), expected_output)

    def test_empty_list(self):
        records = []
        expected_output = []
        self.assertEqual(check_dividend_variances(records), expected_output)

if __name__ == '__main__':
    unittest.main()