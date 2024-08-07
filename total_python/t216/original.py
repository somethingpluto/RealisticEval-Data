def get_local_ip() -> str:
    """
    Method created by ChatGPT
    """
    # Execute the ip command to get addresses
    result = subprocess.run(['ip', 'addr', 'show', 'wlan0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Regular expression to match IPv4 addresses, excluding the loopback address
    ip_pattern = re.compile(r'inet (\d+\.\d+\.\d+\.\d+)/\d+')
    
    # Search for IP addresses in the command output
    ips : list[str] = ip_pattern.findall(result.stdout)
    
    # Optionally, filter out specific interfaces or address ranges
    for ip in ips:
        if ip.startswith("192.168."):
            return ip
    return "No local IP found"
