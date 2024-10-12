def filter_array(unfiltered_array, is_qualified):
    """
    Filters elements from an array based on a qualification function.

    :param unfiltered_array: The array to filter.
    :param is_qualified: The function that determines if an element qualifies.
    :return: A new list containing the elements that qualify.
    """
    filtered_results = []

    # Use a for loop to iterate through each element in the unfiltered array
    for element in unfiltered_array:
        # Check if the current element qualifies
        if is_qualified(element):
            # If it qualifies, append it to the results list
            filtered_results.append(element)

    return filtered_results  # Return the filtered results