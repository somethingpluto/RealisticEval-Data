def reorder_data(image_scores: list[float], image_names: list[str], image_ids: list[str | float]) -> dict[str, list[float] | list[str]]:
    """
    Reorders image questions based on scores in ascending order.

    Args:
        image_scores (list[float]): An array of numerical scores for the images.
        image_names (list[str]): An array of image names corresponding to the scores.
        image_ids (list[str | float]): An array of image IDs corresponding to the scores.

    Returns:
        dict: A dictionary containing the sorted scores, names, and IDs.
            - resultScores (list[float]): A list of sorted numerical scores.
            - resultNames (list[str]): A list of sorted image names.
            - resultIDs (list[str | float]): A list of sorted image IDs.
    """
    pass  # Function implementation goes here