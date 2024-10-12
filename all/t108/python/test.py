class TestReorderData(unittest.TestCase):
    def test_reorder_scores_ascending(self):
        imageScores = [90, 85, 95]
        imageNames = ["image1.png", "image2.png", "image3.png"]
        imageIDs = ["id1", "id2", "id3"]
        result = reorderData(imageScores, imageNames, imageIDs)
        self.assertEqual(result.resultScores, [85, 90, 95])
        self.assertEqual(result.resultNames, ["image2.png", "image1.png", "image3.png"])
        self.assertEqual(result.resultIDs, ["id2", "id1", "id3"])

    def test_scores_already_in_order(self):
        imageScores = [70, 75, 80]
        imageNames = ["imageA.png", "imageB.png", "imageC.png"]
        imageIDs = ["idA", "idB", "idC"]
        result = reorderData(imageScores, imageNames, imageIDs)
        self.assertEqual(result.resultScores, [70, 75, 80])
        self.assertEqual(result.resultNames, ["imageA.png", "imageB.png", "imageC.png"])
        self.assertEqual(result.resultIDs, ["idA", "idB", "idC"])

    def test_single_element(self):
        imageScores = [50]
        imageNames = ["imageSingle.png"]
        imageIDs = ["idSingle"]
        result = reorderData(imageScores, imageNames, imageIDs)
        self.assertEqual(result.resultScores, [50])
        self.assertEqual(result.resultNames, ["imageSingle.png"])
        self.assertEqual(result.resultIDs, ["idSingle"])

    def test_empty_array(self):
        imageScores = []
        imageNames = []
        imageIDs = []
        result = reorderData(imageScores, imageNames, imageIDs)
        self.assertEqual(result.resultScores, [])
        self.assertEqual(result.resultNames, [])
        self.assertEqual(result.resultIDs, [])

    def test_duplicate_scores(self):
        imageScores = [88, 88, 92]
        imageNames = ["image1.png", "image2.png", "image3.png"]
        imageIDs = ["id1", "id2", "id3"]
        result = reorderData(imageScores, imageNames, imageIDs)
        self.assertEqual(result.resultScores, [88, 88, 92])
        self.assertEqual(result.resultNames, ["image1.png", "image2.png", "image3.png"])
        self.assertEqual(result.resultIDs, ["id1", "id2", "id3"])