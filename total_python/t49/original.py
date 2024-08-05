def get_past_k_weekdays_list(range_m, k, reference_date=None):
    """
    Generates a list of dates representing the occurrences of a specific weekday (k) over the past range_m months from a reference date.
    This function finds all occurrences of the specified weekday in each month within the range, including cases where the month might not have a fifth occurrence.
    The function returns a list of dates without future dates or duplicates, sorted in descending order.

    Parameters:
    - range_m (int): The range in months before the reference date from which to generate the list of weekdays.
    - k (int): The weekday for which to generate the list, where Monday is 0 and Sunday is 6.
    - reference_date (datetime.datetime, optional): The reference date from which to calculate the past range. If not provided, today's date is used.

    Returns:
    - list of datetime.datetime: A list of dates for the specified weekday, covering the past range_m months from the reference date,
      excluding future dates and duplicates, sorted in descending order. Each date represents an occurrence of the specified weekday within the range.
    """

    if reference_date is None:
        reference_date = datetime.now()

    k_weekdays_set = set()

    for month_delta in range(range_m):
        target_date = reference_date - relativedelta(months=month_delta)
        y, m = target_date.year, target_date.month
        for week_n in range(1, 6):
            nth_k_weekday = find_nth_weekday_of_specific_year(y, m, week_n, k)
            if nth_k_weekday is not None and nth_k_weekday <= reference_date:
                k_weekdays_set.add(nth_k_weekday)

    k_weekdays_list = sorted(list(k_weekdays_set), reverse=True)
    return k_weekdays_list