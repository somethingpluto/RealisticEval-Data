
from typing import List

def reorder_data(image_scores: List[int], image_names: List[str], image_ids: List[str]) -> dict:
    """
    Sort the images in ascending order based on their scores and return the reordered image score, name, and ID.

    Args:
        image_scores (list[int]): Array of image scores.
        image_names (list[str]): Array of image names corresponding to the scores.
        image_ids (list[str]): Array of image IDs corresponding to the scores.

    Returns:
        dict: A dictionary containing the sorted scores, names, and IDs.
              For example: {'resultScores': sorted_scores,'resultNames': sorted_names,'resultIDs': sorted_ids}
    """
    # Create a dictionary to store the reordered data
    sorted_data = {}

    # Iterate over the image_scores and image_names arrays
    for i in range(len(image_scores)):
        # Iterate over the image_ids arrays
        for j in range(len(image_ids)):
            # If the current image score is higher than the current image name,
            # add the current image score, name, and ID to the dictionary
            if image_scores[i] > image_names[j]:
                sorted_data[image_scores[i], j] = {'score': image_scores[i], 'name': image_names[j], 'id': image_ids[j]}

    # Return the dictionary with the reordered data
    return sorted_data

import unittest


class TestReorderData(unittest.TestCase):
    def test_reorder_scores_ascending(self):
        imageScores = [90, 85, 95]
        imageNames = ["image1.png", "image2.png", "image3.png"]
        imageIDs = ["id1", "id2", "id3"]
        result = reorder_data(imageScores, imageNames, imageIDs)
        self.assertEqual(result['resultScores'], [85, 90, 95])
        self.assertEqual(result['resultNames'], ["image2.png", "image1.png", "image3.png"])
        self.assertEqual(result['resultIDs'], ["id2", "id1", "id3"])

    def test_scores_already_in_order(self):
        imageScores = [70, 75, 80]
        imageNames = ["imageA.png", "imageB.png", "imageC.png"]
        imageIDs = ["idA", "idB", "idC"]
        result = reorder_data(imageScores, imageNames, imageIDs)
        self.assertEqual(result['resultScores'], [70, 75, 80])
        self.assertEqual(result['resultNames'], ["imageA.png", "imageB.png", "imageC.png"])
        self.assertEqual(result['resultIDs'], ["idA", "idB", "idC"])

    def test_single_element(self):
        imageScores = [50]
        imageNames = ["imageSingle.png"]
        imageIDs = ["idSingle"]
        result = reorder_data(imageScores, imageNames, imageIDs)
        self.assertEqual(result['resultScores'], [50])
        self.assertEqual(result['resultNames'], ["imageSingle.png"])
        self.assertEqual(result['resultIDs'], ["idSingle"])

    def test_empty_array(self):
        imageScores = []
        imageNames = []
        imageIDs = []
        result = reorder_data(imageScores, imageNames, imageIDs)
        self.assertEqual(result['resultScores'], [])
        self.assertEqual(result['resultNames'], [])
        self.assertEqual(result['resultIDs'], [])

    def test_duplicate_scores(self):
        imageScores = [88, 88, 92]
        imageNames = ["image1.png", "image2.png", "image3.png"]
        imageIDs = ["id1", "id2", "id3"]
        result = reorder_data(imageScores, imageNames, imageIDs)
        self.assertEqual(result['resultScores'], [88, 88, 92])
        self.assertEqual(result['resultNames'], ["image1.png", "image2.png", "image3.png"])
        self.assertEqual(result['resultIDs'], ["id1", "id2", "id3"])
if __name__ == '__main__':
    unittest.main()