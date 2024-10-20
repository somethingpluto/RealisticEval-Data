# this function was generated by chatgpt
import re
from datetime import timedelta


def gen_timeout_timedelta(s):
    # Define a regex pattern to capture different time units
    pattern = r'(?:(\d+)\s*d)?\s*(?:(\d+)\s*h)?\s*(?:(\d+)\s*m)?\s*(?:(\d+)\s*s)?\s*(?:(\d+)\s*ms)?'
    matches = re.match(pattern, s.strip())

    if not matches:
        raise ValueError("Invalid time format")

    days = int(matches.group(1)) if matches.group(1) else 0
    hours = int(matches.group(2)) if matches.group(2) else 0
    minutes = int(matches.group(3)) if matches.group(3) else 0
    seconds = int(matches.group(4)) if matches.group(4) else 0
    milliseconds = int(matches.group(5)) if matches.group(5) else 0

    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)
