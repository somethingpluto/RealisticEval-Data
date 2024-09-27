import os
import csv
import shutil


def extract_files_excluding_csv(folderA: str, csv_file: str, folderB: str):
    """
    Copy files from folderA to folderB excluding those listed in the specified CSV file.

    Args:
        folderA: Path to the source folder containing all files (str).
        csv_file: Path to the CSV file containing filenames to exclude (str).
        folderB: Path to the destination folder (str).

    Returns:

    """
