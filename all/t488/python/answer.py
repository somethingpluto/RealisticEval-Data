import subprocess
import re
from typing import Optional


def get_local_ip(interface: str = 'Wi-Fi') -> Optional[str]:
    """
    Retrieve the local IP address of the specified network interface on Windows.

    Args:
    interface (str): The name of the network interface to check (default is 'Wi-Fi').

    Returns:
    Optional[str]: The local IP address if found, otherwise None.
    """
    try:
        # Execute the 'ipconfig' command to get addresses for the specified interface
        result = subprocess.run(
            ['ipconfig'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        # Regular expression to match IPv4 addresses
        ip_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')

        # Search for IP addresses in the command output
        ips: list[str] = ip_pattern.findall(result.stdout)

        # Return the first local IP found
        for ip in ips:
            if ip.startswith("192.168."):
                return ip

        return None  # Return None if no suitable IP is found

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
