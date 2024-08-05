import json

def segregate_entries_by_pid(source_path, match_output, non_match_output, target_pids):
    # Load data from the source JSON file
    with open(source_path, 'r') as file:
        entries = json.load(file)

    # Segregate entries based on the presence of 'pid' in the target list
    matched = [entry for entry in entries if 'pid' in entry and entry['pid'] in target_pids]
    unmatched = [entry for entry in entries if 'pid' not in entry or entry['pid'] not in target_pids]

    # Save matched and unmatched entries to respective files
    with open(match_output, 'w') as f1:
        json.dump(matched, f1, indent=4)
    with open(non_match_output, 'w') as f2:
        json.dump(unmatched, f2, indent=4)

    print("Entries have been segregated and saved successfully.")
