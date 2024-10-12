def reorder_data(image_scores, image_names, image_ids):
    """
    Sort the images in ascending order based on their scores and return the reordered image score, name, and ID.

    Args:
        image_scores (list of float): Array of image scores.
        image_names (list of str): Array of image names corresponding to the scores.
        image_ids (list of str): Array of image IDs corresponding to the scores.

    Returns:
        dict: A dictionary containing the sorted scores, names, and IDs.
    """

    # Combine the scores, names, and IDs into a list of dictionaries
    image_data = [
        {'score': score, 'name': image_names[i], 'id': image_ids[i]}
        for i, score in enumerate(image_scores)
    ]

    # Sort the list of dictionaries by score in ascending order
    image_data.sort(key=lambda x: x['score'])

    # Extract sorted scores, names, and IDs into separate lists
    result_scores = [data['score'] for data in image_data]
    result_names = [data['name'] for data in image_data]
    result_ids = [data['id'] for data in image_data]

    # Return the sorted arrays as a dictionary
    return {'resultScores': result_scores, 'resultNames': result_names, 'resultIDs': result_ids}