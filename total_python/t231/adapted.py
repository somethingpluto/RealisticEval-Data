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
