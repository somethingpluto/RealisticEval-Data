from typing import Dict, Optional

def convert_csv_values(row: Dict[str, str]) -> Dict[str, Optional[str]]:
    """
    Convert numeric values in a CSV row from string format to a standardized format.

    Args:
        row (Dict[str, str]): A dictionary representing a row of CSV data where
                               keys are column names and values are strings.

    Returns:
        Dict[str, Optional[str]]: A new dictionary with values converted:
                                   - Numeric strings have commas replaced with dots.
                                   - Non-numeric strings are set to None.
    """