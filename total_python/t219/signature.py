from typing import List


def check_dividend_variances(records: List) -> List:
    """
    Check for ticker symbols with the same ex-dividend date but different dividend amounts.

    Parameters:
    - records (list of tuples): Each tuple contains (ticker, ex_dividend_date, dividend_amount).

    Returns:
    - list of tuples: Each tuple contains (ticker, ex_dividend_date) that have different dividend amounts.
    """
