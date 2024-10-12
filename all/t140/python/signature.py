from datetime import datetime

def get_time_since_born_until_now(birth_date: datetime) -> tuple[int, int, int, int, int]:
    """ 
    Calculate the years, months, days, hours, and minutes that have passed 
    from the birth date to the current date and return them as a tuple. 
    The contents of the tuple are the values of these units.
    
    :param birth_date: The birth date as a datetime object.
    """
    