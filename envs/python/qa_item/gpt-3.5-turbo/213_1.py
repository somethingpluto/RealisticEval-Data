import numpy as np

def im2col(image, filter_height, filter_width, stride=1, padding=0):
    C, H, W = image.shape
    H_padded, W_padded = H + 2*padding, W + 2*padding
    image_padded = np.pad(image, ((0,0), (padding, padding), (padding, padding)), mode='constant')
    
    cols = []
    for i in range(0, H_padded - filter_height + 1, stride):
        for j in range(0, W_padded - filter_width + 1, stride):
            cols.append(image_padded[:, i:i+filter_height, j:j+filter_width].ravel())
    
    return np.array(cols).T
import unittest

import numpy as np


class TestIm2Col(unittest.TestCase):

    def test_single_channel_no_padding_stride_1(self):
        image = np.array([
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
        ])  # Shape (1, 4, 4)
        filter_height = 2
        filter_width = 2
        stride = 1
        padding = 0

        expected_output = np.array([
            [1, 2, 3, 5, 6, 7, 9, 10, 11],
            [2, 3, 4, 6, 7, 8, 10, 11, 12],
            [5, 6, 7, 9, 10, 11, 13, 14, 15],
            [6, 7, 8, 10, 11, 12, 14, 15, 16]
        ])
        output = im2col(image, filter_height, filter_width, stride, padding)
        np.testing.assert_array_equal(output, expected_output)

    def test_single_channel_no_padding_stride_2(self):
        image = np.array([
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
        ])  # Shape (1, 4, 4)
        filter_height = 2
        filter_width = 2
        stride = 2
        padding = 0

        expected_output = np.array([
            [1, 3, 9, 11],
            [2, 4, 10, 12],
            [5, 7, 13, 15],
            [6, 8, 14, 16]
        ])
        output = im2col(image, filter_height, filter_width, stride, padding)
        np.testing.assert_array_equal(output, expected_output)

    def test_multi_channel_no_padding_stride_1(self):
        image = np.array([
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            [[9, 8, 7],
             [6, 5, 4],
             [3, 2, 1]]
        ])  # Shape (2, 3, 3), 2 channels
        filter_height = 2
        filter_width = 2
        stride = 1
        padding = 0

        expected_output = np.array([
            [1, 2, 4, 5],
            [2, 3, 5, 6],
            [4, 5, 7, 8],
            [5, 6, 8, 9],
            [9, 8, 6, 5],
            [8, 7, 5, 4],
            [6, 5, 3, 2],
            [5, 4, 2, 1]
        ])
        output = im2col(image, filter_height, filter_width, stride, padding)
        np.testing.assert_array_equal(output, expected_output)

if __name__ == '__main__':
    unittest.main()