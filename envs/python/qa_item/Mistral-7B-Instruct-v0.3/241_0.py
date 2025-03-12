from typing import Tuple
import os
from collections import defaultdict
from functools import reduce

from difflib import get_close_matches

def get_min_seq_num_and_distance(file_path: str, word1: str, word2: str) -> Tuple[int, int]:
    if not os.path.isfile(file_path):
        return (None, float('inf'))

    with open(file_path, 'r') as f:
        lines = f.readlines()

    word_to_line_num = defaultdict(list)
    for i, line in enumerate(lines):
        words = line.strip().split()
        for word in words:
            word_to_line_num[word].append(i)

    if not word1 in word_to_line_num or not word2 in word_to_line_num:
        return (None, float('inf'))

    line_nums1 = word_to_line_num[word1]
    line_nums2 = word_to_line_num[word2]

    distances = [levenshtein_distance(word1, word) for word in line_nums2]
    min_distance_line_nums = [line_num for line_num, distance in zip(line_nums2, distances) if distance!= float('inf')]

    if not min_distance_line_nums:
        return (None, float('inf'))

    min_distance_line_num = min(min_distance_line_nums)
    min_distance_line = lines[min_distance_line_num]

    words = min_distance_line.strip().split()
    min_distance_word_index1 = words.index(word1)
    min_distance_word_index2 = words.index(word2)

    if min_distance_word_index1 > min_distance_word_index2:
        min_distance_word_index1, min_distance_word_index2 = min_distance_word_index2, min_distance_word_index1

    min_distance_word1_to_word2 = min_distance_word_index2 - min_distance_word_index1

    for line_num in line_nums1:
        if line_num!= min_distance_line_num:
            words = lines[line_num].strip().split()
            distance = min_distance_word1_to_word2 + (words.index(word1) if word1 in words else float('inf')) + (len(words) - words.index(word2) if word2 in words else float('inf'))
            if distance < min_distance:
                min_distance = distance

    return (min_distance_line_num, min_distance)

def levenshtein_distance(s1: str, s2: str) -> int:
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1!= c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]
import unittest
from unittest.mock import mock_open, patch


class TestGetMinDistance(unittest.TestCase):

    def test_basic_functionality(self):
        """ Test basic functionality with expected input """
        mock_content = "hello world\napple banana apple\norange apple banana"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (2, 1))


    def test_words_not_present(self):
        """ Test case where one or both words are not present """
        mock_content = "apple orange pear\norange pear apple"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (None, float('inf')))

    def test_empty_file(self):
        """ Test an empty file """
        with patch('builtins.open', mock_open(read_data='')):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (None, float('inf')))

    def test_multiple_lines_with_varying_distances(self):
        """ Test multiple lines with varying distances between words """
        mock_content = "apple banana\napple orange orange banana\napple orange orange orange banana"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (1, 1))
if __name__ == '__main__':
    unittest.main()