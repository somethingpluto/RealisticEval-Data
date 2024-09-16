import csv
import json


def tsv_to_jsonl(tsv_file_path: str, jsonl_file_path: str) -> None:
    """
    Convert a TSV file to a JSONL file.

    Parameters:
    - tsv_file_path (str): Path to the input TSV file.
    - jsonl_file_path (str): Path to the output JSONL file.
    """
    try:
        with open(tsv_file_path, 'r', newline='', encoding='utf-8') as tsv_file, \
                open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:

            # Create a CSV reader object using the tab delimiter
            tsv_reader = csv.DictReader(tsv_file, delimiter='\t')

            # Write each row as a JSON object to the JSONL file
            for row in tsv_reader:
                jsonl_file.write(json.dumps(row) + '\n')

        print(f"Successfully converted {tsv_file_path} to {jsonl_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")