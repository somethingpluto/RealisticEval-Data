import re
import subprocess

def get_local_ip(interface: str = 'wlan0') -> str:
    """
    Retrieve the local IP address from the specified network interface.

    Args:
    interface (str): The network interface to query. Default is 'wlan0'.

    Returns:
    str: The local IP address, or a message indicating no IP was found.

    Raises:
    RuntimeError: If the subprocess encounters an error or if no suitable IP is found.
    """
    try:
        # Execute the command to get the IP addresses from the specified interface
        result = subprocess.run(['ip', 'addr', 'show', interface],
                                capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        # Handle errors from the subprocess command
        raise RuntimeError(f"Failed to retrieve IP address: {str(e)}")

    # Regular expression to match IPv4 addresses, excluding the loopback address
    ip_pattern = re.compile(r'inet (\d+\.\d+\.\d+\.\d+)/\d+')

    # Search for IP addresses in the command output
    ips = ip_pattern.findall(result.stdout)

    # Return the first valid IP found, or raise an error if no IP is found
    if ips:
        return ips[0]
    else:
        raise RuntimeError("No local IP found")