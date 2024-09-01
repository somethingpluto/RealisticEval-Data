def check_dividend_variances(records):
    """
    Check for ticker symbols with the same ex-dividend date but different dividend amounts.

    Parameters:
    - records (list of tuples): Each tuple contains (ticker, ex_dividend_date, dividend_amount).

    Returns:
    - list of tuples: Each tuple contains (ticker, ex_dividend_date) that have different dividend amounts.
    """
    # Dictionary to store dividend amounts by (ticker, ex_dividend_date)
    dividend_dict = {}

    # Iterate through the records
    for ticker, ex_dividend_date, dividend_amount in records:
        key = (ticker, ex_dividend_date)
        if key not in dividend_dict:
            dividend_dict[key] = set()
        dividend_dict[key].add(dividend_amount)

    # Find entries with more than one unique dividend amount
    result = [(ticker, ex_dividend_date) for (ticker, ex_dividend_date), amounts in dividend_dict.items() if len(amounts) > 1]

    return result
