import numpy as np
import unittest

def process_jiang(raw_data, frequencies):
    """
    Processes the raw measurement data by repeating frequency values
    and reshaping the data into a structured format.

    Parameters:
    raw_data (np.ndarray): A 2D array with shape (num_measurements, 2),
                           where each row contains two data values.
    frequencies (np.ndarray): A 1D array with frequency values,
                              length must match the number of columns in raw_data.

    Returns:
    np.ndarray: A 2D array with shape (num_frequencies * num_measurements, 3),
                where the first column contains the frequencies,
                and the second and third columns contain reshaped raw data values.
    """
    num_frequencies = raw_data.shape[1]
    num_measurements = raw_data.shape[0]
    repeated_frequencies = np.repeat(frequencies, num_measurements)
    processed_data = np.zeros((num_frequencies * num_measurements, 3))
    processed_data[:, 0] = repeated_frequencies
    reshaped_raw_data = raw_data.reshape(-1)
    processed_data[:, 1:] = reshaped_raw_data.reshape(-1, 2)
    return processed_data

class TestProcessJiang(unittest.TestCase):

    def test_case_1(self):
        raw_data = np.array([[1, 2], [3, 4]])
        frequencies = np.array([10])
        expected_output = np.array([[10, 1, 2],
                                     [10, 3, 4]])
        result = process_jiang(raw_data, frequencies)
        np.testing.assert_array_equal(result, expected_output)

    def test_case_2(self):
        raw_data = np.array([[5, 6], [7, 8], [9, 10]])
        frequencies = np.array([20, 30])
        expected_output = np.array([[20, 5, 6],
                                     [20, 7, 8],
                                     [20, 9, 10],
                                     [30, 5, 6],
                                     [30, 7, 8],
                                     [30, 9, 10]])
        result = process_jiang(raw_data, frequencies)
        np.testing.assert_array_equal(result, expected_output)




if __name__ == '__main__':
    unittest.main()
