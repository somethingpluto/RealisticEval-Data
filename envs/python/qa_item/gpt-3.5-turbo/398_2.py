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
    # Read the CSV file to get the list of filenames to exclude
    exclude_files = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            exclude_files.extend(row)
    
    # Copy files from folderA to folderB excluding those in exclude_files list
    for file_name in os.listdir(folderA):
        if file_name not in exclude_files:
            source_path = os.path.join(folderA, file_name)
            destination_path = os.path.join(folderB, file_name)
            shutil.copyfile(source_path, destination_path)
import os
import shutil
import unittest


class TestExtractFiles(unittest.TestCase):

    def setUp(self):
        """Set up test directories and files before each test case."""
        self.folderA = "test_folderA"
        self.folderB = "test_folderB"
        os.makedirs(self.folderA, exist_ok=True)
        os.makedirs(self.folderB, exist_ok=True)

    def tearDown(self):
        """Clean up the test directories after each test case."""
        shutil.rmtree(self.folderA)
        shutil.rmtree(self.folderB)

    def create_csv(self, filename_list):
        """Helper method to create a CSV file for testing."""
        csv_file = "test_exclude.csv"
        with open(csv_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["filename"])  # Write header
            for name in filename_list:
                writer.writerow([name])
        return csv_file

    def test_basic_functionality(self):
        """Test basic functionality with some files excluded."""
        with open(os.path.join(self.folderA, "file1.txt"), "w") as f:
            f.write("Content of file 1")
        with open(os.path.join(self.folderA, "file2.txt"), "w") as f:
            f.write("Content of file 2")
        with open(os.path.join(self.folderA, "file3.txt"), "w") as f:
            f.write("Content of file 3")

        csv_file = self.create_csv(["file2.txt"])  # Exclude file2.txt
        extract_files_excluding_csv(self.folderA, csv_file, self.folderB)

        self.assertTrue(os.path.exists(os.path.join(self.folderB, "file1.txt")))
        self.assertFalse(os.path.exists(os.path.join(self.folderB, "file2.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.folderB, "file3.txt")))

    def test_empty_folderA(self):
        """Test when folderA is empty."""
        csv_file = self.create_csv(["file1.txt"])  # Exclude file1.txt
        extract_files_excluding_csv(self.folderA, csv_file, self.folderB)

        self.assertEqual(len(os.listdir(self.folderB)), 0)

    def test_all_files_excluded(self):
        """Test when all files are excluded."""
        with open(os.path.join(self.folderA, "file1.txt"), "w") as f:
            f.write("Content of file 1")
        with open(os.path.join(self.folderA, "file2.txt"), "w") as f:
            f.write("Content of file 2")

        csv_file = self.create_csv(["file1.txt", "file2.txt"])  # Exclude all files
        extract_files_excluding_csv(self.folderA, csv_file, self.folderB)

        self.assertEqual(len(os.listdir(self.folderB)), 0)

    def test_destination_folder_already_has_files(self):
        """Test when folderB already contains files."""
        with open(os.path.join(self.folderB, "existing_file.txt"), "w") as f:
            f.write("This is an existing file.")

        with open(os.path.join(self.folderA, "file1.txt"), "w") as f:
            f.write("Content of file 1")

        csv_file = self.create_csv([])  # Do not exclude any files
        extract_files_excluding_csv(self.folderA, csv_file, self.folderB)

        # Check if both existing and new files are present
        self.assertTrue(os.path.exists(os.path.join(self.folderB, "existing_file.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.folderB, "file1.txt")))

    def test_empty_csv_file(self):
        """Test with an empty CSV file."""
        with open(os.path.join(self.folderA, "file1.txt"), "w") as f:
            f.write("Content of file 1")

        csv_file = self.create_csv([])  # Empty CSV, do not exclude any files
        extract_files_excluding_csv(self.folderA, csv_file, self.folderB)

        self.assertTrue(os.path.exists(os.path.join(self.folderB, "file1.txt")))
if __name__ == '__main__':
    unittest.main()