import csv


def clean_csv(input_file_path, output_file_path):
    """
    Processes a CSV file, deleting rows that end with two consecutive empty columns.

    :param input_file_path: Path to the input CSV file.
    :param output_file_path: Path to the output CSV file where cleaned data will be stored.
    """
    with open(input_file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    # Filter rows that do not end with two consecutive empty columns
    cleaned_rows = [row for row in rows if len(row) < 2 or (row[-1] != '' or row[-2] != '')]

    with open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_rows)
