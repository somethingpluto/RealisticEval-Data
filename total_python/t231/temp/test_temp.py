import json
import unittest
from unittest.mock import mock_open, patch


class TestReadLog(unittest.TestCase):

    def test_read_correct_data(self):
        """ Test reading correctly formatted JSON lines """
        mock_file_content = '{"test_acc1": 88.5, "train_loss": 0.75}\n' \
                            '{"test_acc1": 89.0, "train_loss": 0.70}'
        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            train_loss, test_acc1 = read_log("dummy_path.json")
            self.assertEqual(train_loss, [0.75, 0.70])
            self.assertEqual(test_acc1, [88.5, 89.0])

    def test_file_not_found(self):
        """ Test behavior when the file does not exist """
        with patch('builtins.open', side_effect=FileNotFoundError):
            train_loss, test_acc1 = read_log("nonexistent_path.json")
            self.assertEqual(train_loss, [])
            self.assertEqual(test_acc1, [])

    def test_invalid_json(self):
        """ Test behavior when file contains invalid JSON """
        mock_file_content = '{"test_acc1": 88.5, "train_loss": 0.75}\nInvalid JSON Line'
        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            with patch('json.loads', side_effect=json.JSONDecodeError("Expecting value", "doc", 0)):
                train_loss, test_acc1 = read_log("dummy_path.json")
                self.assertEqual(train_loss, [])
                self.assertEqual(test_acc1, [])

    def test_empty_file(self):
        """ Test reading an empty file """
        with patch('builtins.open', mock_open(read_data="")):
            train_loss, test_acc1 = read_log("empty_file.json")
            self.assertEqual(train_loss, [])
            self.assertEqual(test_acc1, [])

    def test_partial_data_entries(self):
        """ Test file with missing fields in some entries """
        mock_file_content = '{"test_acc1": 88.5, "train_loss": 0.75}\n' \
                            '{"test_acc1": 90.0}'  # Missing train_loss
        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            train_loss, test_acc1 = read_log("partial_data_file.json")
            self.assertEqual(train_loss, [0.75])  # Only one complete entry
            self.assertEqual(test_acc1, [88.5, 90.0])

import json


def read_log(log_file_path):
    try:
        with open(log_file_path, "r") as file:
            data_entries = [json.loads(line) for line in file]
    except FileNotFoundError:
        print(f"Error: The file {log_file_path} does not exist.")
        return [], []
    except json.JSONDecodeError:
        print(f"Error: The file {log_file_path} contains invalid JSON.")
        return [], []

    # Using get with default values to handle missing keys
    train_loss_list = [entry.get("train_loss") for entry in data_entries if "train_loss" in entry]
    test_acc1_list = [entry.get("test_acc1") for entry in data_entries if "test_acc1" in entry]

    return train_loss_list, test_acc1_list