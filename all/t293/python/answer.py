def reorder_data(image_scores, image_names, image_ids):
    # Combine scores, names, and IDs into a list of dictionaries
    image_data = [
        {'score': score, 'name': image_names[index], 'id': image_ids[index]}
        for index, score in enumerate(image_scores)
    ]
    
    # Sort image_data by scores in ascending order
    image_data.sort(key=lambda x: x['score'])
    
    # Separate the sorted image_data back into separate lists
    result_scores = []
    result_names = []
    result_ids = []
    
    for data in image_data:
        result_scores.append(data['score'])
        result_names.append(data['name'])
        result_ids.append(data['id'])
    
    return {
        'resultScores': result_scores,
        'resultNames': result_names,
        'resultIDs': result_ids
    }