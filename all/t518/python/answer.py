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
    converted_row = {}
    
    for key, value in row.items():
        # Check if the value is numeric with possible comma and negative sign
        is_numeric = value.replace(',', '', 1).replace('-', '', 1).isdigit()
        
        if is_numeric:
            # Replace comma with dot for numeric conversion
            converted_row[key] = value.replace(',', '.')
        else:
            # Set to None if not a valid number
            converted_row[key] = None
            
    return converted_row