def is_cron_between_2_and_4_am(cron_expression):
    # Split the cron expression by spaces
    parts = cron_expression.split(' ')

    # Get the hour part (second part in the cron expression)
    hour_part = parts[1]

    # Split the hour part by comma and convert it to a list of integers
    hours = list(map(int, hour_part.split(',')))

    # Check if any hour is between 2 (inclusive) and 4 (exclusive)
    return any(2 <= hour < 4 for hour in hours)
