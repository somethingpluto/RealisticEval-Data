from datetime import datetime


def get_timestamp(created_at: datetime) -> str:
    """Computes the difference between the specified date and the current time, returning it in a human-readable way.
    
    Args:
        created_at (datetime): The date to calculate the time difference from.
        
    Returns:
        str: A string indicating the time elapsed, e.g., "3 days ago", "5 hours ago".
    """
