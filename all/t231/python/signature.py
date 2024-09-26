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
