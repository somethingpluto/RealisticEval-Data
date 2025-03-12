def read_log(log_file_path):
    """
    Reads a log file containing JSON entries and extracts training loss and test accuracy.
    Json entries such as {"test_acc1": 88.5, "train_loss": 0.75}
    Args:
        log_file_path (str): The path to the log file to be read.

    Returns:
        tuple: A tuple containing two lists:
            - train_loss_list (list): A list of training loss values extracted from the log.
            - test_acc1_list (list): A list of test accuracy values extracted from the log.
    """
    train_loss_list = []
    test_acc1_list = []

    with open(log_file_path, 'r') as file:
        for line in file:
            try:
                log_entry = json.loads(line)
                if 'train_loss' in log_entry:
                    train_loss_list.append(log_entry['train_loss'])
                if 'test_acc1' in log_entry:
                    test_acc1_list.append(log_entry['test_acc1'])
            except json.JSONDecodeError:
                continue

    return train_loss_list, test_acc1_list
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

    def test_read_correct_data_single(self):
        """ Test reading correctly formatted JSON lines """
        mock_file_content = '{"test_acc1": 88.5, "train_loss": 0.75}'
        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            train_loss, test_acc1 = read_log("dummy_path.json")
            self.assertEqual(train_loss, [0.75])
            self.assertEqual(test_acc1, [88.5])
    def test_empty_file(self):
        """ Test reading an empty file """
        with patch('builtins.open', mock_open(read_data="")):
            train_loss, test_acc1 = read_log("empty_file.json")
            self.assertEqual(train_loss, [])
            self.assertEqual(test_acc1, [])

    def test_partial_data_entries(self):
        """ Test file with missing fields in some entries """
        mock_file_content = '{"test_acc1": 88.5, "train_loss": 0.75}\n' \
                            '{"test_acc1": 90.0,"train_loss": 0.75,"f1":0.91}'  # Missing train_loss
        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            train_loss, test_acc1 = read_log("partial_data_file.json")
            self.assertEqual(train_loss, [0.75, 0.75])  # Only one complete entry
            self.assertEqual(test_acc1, [88.5, 90.0])

if __name__ == '__main__':
    unittest.main()