import csv
import os
from pandas import DataFrame
from pathlib import Path
from string import Template

# NOTE: Generated by ChatGPT - not sure if buggy
def append_or_skip_row(file_handler, reader, row_candidate):
    """
    Appends a new row to a CSV file if there isn't a row with matching values in the first three columns.
    
    :param file_handler: File handler of the CSV file opened in read-plus mode ('r+').
    :param new_row: List containing the new row to be appended.
    """
    
    # Read all existing rows into a list
    existing_rows = list(reader)
    
    row_candidate_str = csv_row_tpl.substitute(row_candidate)
    print(f"Row candidate str:\n {row_candidate_str}")
    
    # Check if a row with matching first three columns exists
    for row in existing_rows:
        if row[:3] == row_candidate_str[:3]:
            print("A row with matching first three columns already exists. Skipping append.")
            return
    
    # Move to the end of the file to append the new row
    file_handler.seek(0, 2)
    file_handler.write(row_candidate_str + "\n")
    
    print("New row appended successfully.")