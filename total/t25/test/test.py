import unittest
import os

class TestJsonFiltering(unittest.TestCase):
    def setUp(self):
        # Create a sample JSON data file
        self.test_data = [
            {"name": "Alice", "pid": 123},
            {"name": "Bob"},
            {"name": "Charlie", "pid": 456}
        ]
        self.input_file = 'test_input.json'
        with open(self.input_file, 'w') as file:
            json.dump(self.test_data, file)

        self.output_file1 = 'test_output_matched.json'
        self.output_file2 = 'test_output_unmatched.json'

    def test_filter_json(self):
        # Run the segregation function
        target_pids = [123]
        segregate_entries_by_pid(self.input_file, self.output_file1, self.output_file2, target_pids)

        # Check output files for correctness
        with open(self.output_file1, 'r') as f1:
            matched_data = json.load(f1)
        with open(self.output_file2, 'r') as f2:
            unmatched_data = json.load(f2)

        self.assertEqual(len(matched_data), 1)
        self.assertEqual(matched_data[0]['pid'], 123)
        self.assertEqual(len(unmatched_data), 2)

    def tearDown(self):
        # Clean up created files
        os.remove(self.input_file)
        os.remove(self.output_file1)
        os.remove(self.output_file2)

# Run tests
if __name__ == '__main__':
    unittest.main()
