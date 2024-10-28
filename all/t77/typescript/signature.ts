/**
 * Formats the given timestamp as a string according to the specified format, using the system's local time zone.
 *
 * @param timestamp - The time value representing the seconds since the epoch.
 * @param date_format - The format string to use for formatting the timestamp. Defaults to '%a %b %d %I:%M:%S %p %z %Y'.
 * @returns The formatted date and time string.
 */
function formatTimestampToString(timestamp: number, date_format: string = 'ccc LLL d hh:mm:ss a zzzz yyyy'): string {}