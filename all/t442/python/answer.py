from typing import Dict, List, Union


def convert_strings_to_numbers(data:Union[Dict,List])->Union[Dict,List]:
    """
    Convert strings in nested structures (e.g. dictionaries, arrays) to numbers (integers or floating point numbers) as much as possible

    Args:
        data (Union[Dict,List]): before convert data

    Returns:
        Union[Dict,List]: after convert data
    """
    if isinstance(data, dict):
        return {key: convert_strings_to_numbers(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_strings_to_numbers(item) for item in data]
    elif isinstance(data, str):
        try:
            if '.' in data:
                return float(data)
            else:
                return int(data)
        except ValueError:
            return data 
    else:
        return data  