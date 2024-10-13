from datetime import datetime, timedelta

def get_timestamp(created_at: datetime) -> str:
    now = datetime.now()
    diff_in_seconds = int((now - created_at).total_seconds())
    
    # Define time intervals in seconds
    intervals = {
        'year': 31536000,
        'month': 2592000,
        'week': 604800,
        'day': 86400,
        'hour': 3600,
        'minute': 60,
    }
    
    # Determine the most appropriate time interval and its unit
    interval_count = 0
    interval_unit = ''
    
    if diff_in_seconds >= intervals['year']:
        interval_count = diff_in_seconds // intervals['year']
        interval_unit = 'year' if interval_count == 1 else 'years'
    elif diff_in_seconds >= intervals['month']:
        interval_count = diff_in_seconds // intervals['month']
        interval_unit = 'month' if interval_count == 1 else 'months'
    elif diff_in_seconds >= intervals['week']:
        interval_count = diff_in_seconds // intervals['week']
        interval_unit = 'week' if interval_count == 1 else 'weeks'
    elif diff_in_seconds >= intervals['day']:
        interval_count = diff_in_seconds // intervals['day']
        interval_unit = 'day' if interval_count == 1 else 'days'
    elif diff_in_seconds >= intervals['hour']:
        interval_count = diff_in_seconds // intervals['hour']
        interval_unit = 'hour' if interval_count == 1 else 'hours'
    elif diff_in_seconds >= intervals['minute']:
        interval_count = diff_in_seconds // intervals['minute']
        interval_unit = 'minute' if interval_count == 1 else 'minutes'
    else:
        interval_count = diff_in_seconds
        interval_unit = 'second' if interval_count == 1 else 'seconds'
    
    return f"{interval_count} {interval_unit} ago"