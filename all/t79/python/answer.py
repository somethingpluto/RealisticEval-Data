from datetime import datetime


def generate_date_range_string(start_date: str, end_date: str) -> str:
    """
    Generate a formatted date range string.

    Args:
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    str: A string representing the date range in a human-readable format.

    Raises:
    ValueError: If the start_date or end_date are not in the correct format or if start_date is after end_date.
    """
    try:
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')

        if start_dt > end_dt:
            raise ValueError("start_date cannot be after end_date.")
    except ValueError as e:
        raise ValueError(f"Date must be in 'YYYY-MM-DD' format. {e}")

    start_month = start_dt.strftime('%B')
    end_month = end_dt.strftime('%B')
    start_day = str(start_dt.day)
    end_day = str(end_dt.day)
    start_year = str(start_dt.year)
    end_year = str(end_dt.year)

    # Format output based on whether dates are within the same month and/or year
    if start_year != end_year:
        return f"{start_month} {start_day}, {start_year} to {end_month} {end_day}, {end_year}"
    elif start_month == end_month:
        return f"{start_month} {start_day} to {end_day}, {start_year}"
    else:
        return f"{start_month} {start_day} to {end_month} {end_day}, {start_year}"
