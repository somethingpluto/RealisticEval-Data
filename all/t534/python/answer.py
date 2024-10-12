def remove_element_in_array(array, element):
    # Create a new list to avoid modifying the original
    new_array = []

    # A flag to check if the element has been removed
    removed = False

    # Iterate through the original array
    for item in array:
        if item != element:
            new_array.append(item)  # Add elements that are not the target element
        else:
            if not removed:
                removed = True  # Mark that we've removed the element
                continue  # Skip the first occurrence of the element

    # Return a new list that does not include the specified element
    return new_array
