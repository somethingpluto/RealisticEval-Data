def reorder_data(image_scores: list[int], image_names: list[str], image_ids: list[str]) -> dict:
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