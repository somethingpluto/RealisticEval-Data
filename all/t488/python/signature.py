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
