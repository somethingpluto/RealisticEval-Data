import json


def classify_json_objects_by_pid(source_file, pid_list, match_file, mismatch_file):
    """
    Reads JSON data from a file, filters objects based on 'pid' field inclusion in 'pid_list'.
    Writes matches and mismatches to separate JSON files.

    Args:
    source_file (str): Path to the source JSON file.
    pid_list (list): List of pids to match.
    match_file (str): Path to save matching objects JSON.
    mismatch_file (str): Path to save mismatching objects JSON.
    """
    try:

        # Load data from the source JSON file
        with open(source_file, 'r') as file:
            data = json.load(file)
        # Initialize lists for matches and mismatches
        matches = []
        mismatches = []

        # Classify each object based on 'pid' presence in 'pid_list'
        for obj in data:
            if obj.get('pid') in pid_list:
                matches.append(obj)
            else:
                mismatches.append(obj)

        # Save the matches to a new JSON file
        with open(match_file, 'w') as file:
            json.dump(matches, file, indent=4)

        # Save the mismatches to another JSON file
        with open(mismatch_file, 'w') as file:
            json.dump(mismatches, file, indent=4)

        print("Classification complete. Data saved to respective files.")

    except Exception as e:
        print(f"An error occurred: {e}")
