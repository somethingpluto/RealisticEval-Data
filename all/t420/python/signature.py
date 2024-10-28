from ast import Tuple


def get_min_distance_between_2_word(file_path:str, word1:str, word2:str) -> Tuple:
    """
    Find the minimum distance between two specified words (word1 and word2) from the file and return in which line the distance occurred

    Args:
        file_path (str): file path str
        word1 (str): specified word1 
        word2 (str): specified word2

    Returns:
        Tuple: line the distance between two word
    """