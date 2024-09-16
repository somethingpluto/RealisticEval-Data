

def format_datetime_str(mtime, format='%a %b %d %I:%M:%S %p %z %Y'):
    # Using "localtime" to use the system's local timezone
    tz = zoneinfo.ZoneInfo("localtime")
    dt = datetime.fromtimestamp(mtime, tz)
    return dt.strftime(format)