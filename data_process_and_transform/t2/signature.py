from typing import Any, Optional


def parse_and_format(input_data: Optional[Any]) -> Optional[str]:
    """
    Parse the input data and format it as a comma-separated string.

    Args:
        input_data (Optional[Any]): The input data which could be a string or a list.

    Returns:
        Optional[str]: A comma-separated string or None if input_data is None.
    """