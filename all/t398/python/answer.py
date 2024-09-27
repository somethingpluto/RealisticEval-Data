import os
import csv
import shutil

def extract_files_excluding_csv(folderA, csv_file, folderB):
    """
    Copy files from folderA to folderB excluding those listed in the specified CSV file.

    :param folderA: Path to the source folder containing all files (str).
    :param csv_file: Path to the CSV file containing filenames to exclude (str).
    :param folderB: Path to the destination folder (str).
    """
    # Ensure folderB exists
    os.makedirs(folderB, exist_ok=True)

    # Read the filenames from the CSV file
    filenames = []
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            filenames.append(row[0])

    # Copy all files from folderA to folderB that are not in the CSV file
    for file in os.listdir(folderA):
        if file not in filenames:
            src = os.path.join(folderA, file)
            dst = os.path.join(folderB, file)
            shutil.copy2(src, dst)  # Copy file along with metadata