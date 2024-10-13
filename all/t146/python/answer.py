import math
from typing import Optional, Dict

def format_bytes(bytes: int, options: Optional[Dict[str, Optional[int]]] = None) -> str:
    if options is None:
        options = {}

    decimals = options.get('decimals', 0)
    size_type = options.get('sizeType', 'normal')

    size_units = ["Bytes", "KiB", "MiB", "GiB", "TiB"] if size_type == "accurate" else ["Bytes", "KB", "MB", "GB", "TB"]

    if bytes == 0:
        return "0 Byte"

    unit_index = math.floor(math.log(bytes, 1024)) if bytes > 0 else 0
    formatted_size = f"{bytes / (1024 ** unit_index):.{decimals}f}"

    return f"{formatted_size} {size_units[unit_index] if unit_index < len(size_units) else 'Bytes'}"