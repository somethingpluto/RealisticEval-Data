def find_duplicates_excluding_ips(ip_list, ignore_list):
    """
    Find duplicate IPs in the given IP list excluding specified IPs to ignore.

    :param ip_list: List of IP addresses (strings).
    :param ignore_list: List of IP addresses to ignore (strings).
    :return: A list of duplicate IPs excluding those in the ignore list.
    """
    # Convert ignore_list to a set for faster lookups
    ignore_set = set(ignore_list)

    # Dictionary to count occurrences of each IP
    ip_count = {}

    # Count occurrences of each IP, excluding ignored IPs
    for ip in ip_list:
        if ip not in ignore_set:
            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1

    # Collect duplicate IPs
    duplicates = [ip for ip, count in ip_count.items() if count > 1]

    return duplicates