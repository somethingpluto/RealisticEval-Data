from datetime import datetime, timedelta

def get_time_since_born_until_now(birth_date: datetime) -> tuple[int, int, int, int, int]:
    now = datetime.now()
    
    # Calculate years
    years = now.year - birth_date.year
    
    # Calculate months
    months = now.month - birth_date.month
    if months < 0:
        years -= 1
        months += 12

    # Calculate days
    days = now.day - birth_date.day
    if days < 0:
        months -= 1
        # Set tempDate to the last day of the previous month
        previous_month = (now.replace(day=1) - timedelta(days=1)).day
        days += previous_month

    # Calculate hours
    hours = now.hour - birth_date.hour
    if hours < 0:
        days -= 1
        hours += 24

    # Calculate minutes
    minutes = now.minute - birth_date.minute
    if minutes < 0:
        hours -= 1
        minutes += 60

    return (years, months, days, hours, minutes)