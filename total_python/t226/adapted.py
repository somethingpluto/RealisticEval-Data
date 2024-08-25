import json


def convert_tsv_to_jsonl(tsv_file_path, jsonl_file_path, columns):
    """
    Converts data from a TSV file to a JSONL file based on specified columns.

    Args:
    tsv_file_path (str): The file path to the source TSV file.
    jsonl_file_path (str): The file path to the target JSONL file.
    columns (list of str): A list of column names to extract from the TSV and include in the JSONL.

    Raises:
    KeyError: If any specified column does not exist in the TSV header.
    """
    with open(tsv_file_path, 'r') as tsvfile, open(jsonl_file_path, 'w') as jsonlfile:
        # Read the header to determine column indexes
        header = tsvfile.readline().strip().split('\t')
        indexes = {column: header.index(column) for column in columns}  # Raises KeyError if column not found

        # Process each line in the TSV file
        for line in tsvfile:
            fields = line.strip().split('\t')
            # Extract the fields based on the column indexes and create a dictionary
            instance = {column: fields[indexes[column]] for column in columns}
            # Write the dictionary as a JSON string to the JSONL file
            jsonlfile.write(json.dumps(instance) + '\n')
