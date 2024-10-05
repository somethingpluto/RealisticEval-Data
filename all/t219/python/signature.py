from typing import List


def check_dividend_variances(records: List) -> List:
    """
    Check for ticker symbols with the same ex-dividend date but different dividend amounts.
    Args:
        records (List): Each tuple contains (ticker, ex_dividend_date, dividend_amount).

    Returns:
        List: Each tuple contains (ticker, ex_dividend_date) that have different dividend amounts.
    """