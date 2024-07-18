from typing import Optional, Any


def parse_to_list(input_str: Optional[Any]):
    if input_str is None:
        return None

    if isinstance(input_str, list):
        return ", ".join(input_str)

    items = []

    # Split the input string by lines
    lines = str(input_str).strip().splitlines()

    for line in lines:
        # Check if the line has asterisks or commas, handle both cases
        if '*' in line:
            # Handle lines prefixed with '*'
            items.extend([item.strip() for item in line.split('*') if item.strip()])
        elif ';' in line:
            items.extend([item.strip() for item in line.split(',') if item.strip()])
        elif ',' in line:
            items.extend([item.strip() for item in line.split(';') if item.strip()])
        else:
            items.append(line)

    cleaned_items = []
    for item in items:
        cleaned_item = item.strip()
        if cleaned_item:
            cleaned_items.append(item)

    return ", ".join(repr(item) for item in cleaned_items)