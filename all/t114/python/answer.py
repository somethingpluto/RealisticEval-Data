from typing import List, Dict
from datetime import datetime

def sort_by_timestamp(array: List[Dict]) -> List[Dict]:
    """
    Sorts a list of dictionaries by the 'timestamp' key.

    Args:
        array (List[Dict]): The list of dictionaries to be sorted.

    Returns:
        List[Dict]: The sorted list, based on the 'timestamp' key.
    """
    return sorted(array, key=lambda x: datetime.strptime(x['timestamp'], "%Y-%m-%dT%H:%M:%SZ"))