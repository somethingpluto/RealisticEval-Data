from typing import List


def reorder_data(image_scores: List[int], image_names: List[str], image_ids: List[str]) -> dict:
    """
    Sort the images in ascending order based on their scores and return the reordered image score, name, and ID.

    Args:
        image_scores (list[int]): Array of image scores.
        image_names (list[str]): Array of image names corresponding to the scores.
        image_ids (list[str]): Array of image IDs corresponding to the scores.

    Returns:
        dict: A dictionary containing the sorted scores, names, and IDs.
              For example: {'resultScores': sorted_scores, 'resultNames': sorted_names, 'resultIDs': sorted_ids}
    """
