from typing import List


def bits_to_bytes(bits: List[int]) -> bytearray:
    """
    convert an array of binary bits to an array of bytes. Traversing through each bit, composing these bits into bytes, forming a byte every 8 bits, and then storing these bytes in an array and returning it. If the length of the bit array is not a multiple of 8, the last incomplete byte will be discarded.

    Args:
        bits (List[int]): The input array of bits (each element should be 0 or 1).

    Returns:
        An array of bytes constructed from the bits.
    """