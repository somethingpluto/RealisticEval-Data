from typing import List


def find_shiftjis_not_gbk() -> List:
    """
    find all the characters that can be represented in Shift-JIS, but not in GBK, and return them as an array

    Returns:
        list: A list of characters that are unique to Shift-JIS, not encodable in GBK.
    """
