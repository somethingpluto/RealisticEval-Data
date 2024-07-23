def find_nth_weekday_delta_months_ago(delta_m, n, k, reference_date=None):
    """
    Calculates the date of the nth occurrence of a specific weekday (k) in the month delta_m months before a reference date.
    If the nth occurrence does not exist within that month, it returns the last occurrence of that weekday in the month.
    This function handles cases where the nth weekday might not be present, by providing the closest previous weekday in such cases.
    If no reference date is provided, the current date is used as the reference.

    Parameters:
    - delta_m (int): The number of months before the reference date for which to calculate the weekday's occurrence.
    - n (int): The nth occurrence of the weekday to be calculated. For example, 1 for the first occurrence, 2 for the second, etc.
    - k (int): The weekday, where Monday is 0 and Sunday is 6.
    - reference_date (datetime.datetime, optional): The reference date from which to count back delta_m months. If not provided, today's date is used.

    Returns:
    - datetime.datetime: The calculated date of the nth occurrence of the weekday in the specified month.
      If the nth occurrence does not exist, returns the date of the last occurrence of that weekday in the month.
    """

    # 参照日が指定されていない場合は、今日の日付を使用
    if reference_date is None:
        reference_date = datetime.now()

    # delta_mヶ月前の日付を計算
    target_date = reference_date - relativedelta(months=delta_m)
    y, m = target_date.year, target_date.month

    # 指定された年月の第n週のk曜日を計算
    nth_k_weekday = find_nth_weekday_of_specific_year(y, m, n, k)
    return nth_k_weekday