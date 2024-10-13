def extract_json(response: str) -> str:
    start_pos = response.find('{')  # Find the position of the first '{'

    if start_pos == -1:  # If not found, return an empty string
        return ""

    brace_count = 0  # To track the balance of braces
    end_pos = start_pos  # Initialize end_pos to start_pos

    for i in range(start_pos, len(response)):
        if response[i] == '{':
            brace_count += 1  # Increment for every '{'
        elif response[i] == '}':
            brace_count -= 1  # Decrement for every '}'

        # If brace_count returns to zero, we found the complete JSON object
        if brace_count == 0:
            end_pos = i  # Set end_pos to the current position
            break  # Break out of the loop

    # If brace_count is not zero, it means there was an imbalance (unmatched braces)
    if brace_count != 0:
        return ""  # Return empty string if JSON is incomplete

    # Extract and return the substring that represents the JSON object
    return response[start_pos:end_pos + 1]
