/**
 * @brief Reads a log file containing JSON entries and extracts training loss and test accuracy.
 * Json entries such as {"test_acc1": 88.5, "train_loss": 0.75}
 *
 * @param log_file_path The path to the log file to be read.
 * @return A pair of vectors containing two lists:
 *         - train_loss_list: A vector of training loss values extracted from the log.
 *         - test_acc1_list: A vector of test accuracy values extracted from the log.
 */
std::pair<std::vector<double>, std::vector<double>> read_log(const std::string& log_file_path){}
