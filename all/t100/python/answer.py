import re


def convert_time(duration):
    """
    Converts an ISO 8601 duration string into a more readable format.

    Args:
        duration (str): The ISO 8601 duration string (e.g., "PT1H23M45.678S").

    Returns:
        str: A human-readable duration string (e.g., "1h23m45s678ms").
    """
    # Regex to match ISO 8601 duration format
    regex = r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)(\.\d+)?S)?'
    matches = re.match(regex, duration)

    # Return an empty string if the input doesn't match the expected format
    if not matches:
        return ''

    # Unpacking matches
    hours, minutes, seconds, fractional_seconds = matches.groups()
    converted_time = ''

    # Construct the human-readable duration string
    if hours:
        converted_time += f'{hours}h'
    if minutes:
        converted_time += f'{minutes}m'
    if seconds:
        converted_time += f'{seconds}s'

    if fractional_seconds:
        milliseconds = round(float(fractional_seconds) * 1000)
        if milliseconds > 0:
            converted_time += f'{milliseconds}ms'

    return converted_time
