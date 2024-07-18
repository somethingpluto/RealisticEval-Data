from typing import Optional, Any


def parse_str_to_list_with_delimiter(input_str: Optional[Any]) -> Optional[str]:
    if input_str is None:
        return None

    if isinstance(input_str, list):
        return ", ".join(input_str)

    items = []
    lines = str(input_str).strip().splitlines()

    for line in lines:
        if '*' in line:
            items.extend([item.strip() for item in line.split('*') if item.strip()])
        elif ',' in line:
            items.extend([item.strip() for item in line.split(',') if item.strip()])
        elif ';' in line:
            items.extend([item.strip() for item in line.split(';') if item.strip()])
        else:
            items.append(line.strip())

    return ", ".join(repr(item) for item in items if item)
