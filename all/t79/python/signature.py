def generate_date_range_string(start_date: str, end_date: str) -> str:
    """
    Generates a string based on the entered start and end dates. If the start date and end date are in the same month, only one month will be displayed. If not, the start and end months will be displayed separately. For example, if you enter the start date and end date as,"2023-08-01" and "2023-08-15" respectively, you will finally output "August 1 to 15, 2023".

    For example:
        input:
            start_date: 2023-08-01
            end_date: 2023-08-15
        output:
            August 1 to 15, 2023

    Args:
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
        str: A string representing the date range in a human-readable format.
    """
