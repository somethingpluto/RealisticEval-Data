import math


class Tester(unittest.TestCase):

    def test_find_k_nearest_neighbors_simple_case(self):
        knn = Answer()
        points = [
            Answer.Point(1, 2),
            Answer.Point(3, 4),
            Answer.Point(1, -1),
            Answer.Point(5, 2)
        ]
        query_point = Answer.Point(2, 2)
        k = 2
        result = knn.findKNearestNeighbors(points, query_point, k)

        self.assertEqual(len(result), 2)
        self.assertTrue(self.contains_point(result, Answer.Point(1, 2)))
        self.assertTrue(self.contains_point(result, Answer.Point(3, 4)))

    def test_find_k_nearest_neighbors_exact_match(self):
        knn = Answer()
        points = [
            Answer.Point(1, 2),
            Answer.Point(2, 2),
            Answer.Point(3, 3)
        ]
        query_point = Answer.Point(2, 2)
        k = 1
        result = knn.findKNearestNeighbors(points, query_point, k)

        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0].x, 2.0, delta=0.001)
        self.assertAlmostEqual(result[0].y, 2.0, delta=0.001)

    def test_find_k_nearest_neighbors_larger_k(self):
        knn = Answer()
        points = [
            Answer.Point(1, 2),
            Answer.Point(3, 4),
            Answer.Point(1, -1),
            Answer.Point(5, 2)
        ]
        query_point = Answer.Point(2, 2)
        k = 5  # k is larger than the number of points
        result = knn.findKNearestNeighbors(points, query_point, k)

        self.assertEqual(len(result), 4)

    def test_find_k_nearest_neighbors_empty_points(self):
        knn = Answer()
        points = []
        query_point = Answer.Point(2, 2)
        k = 3
        result = knn.findKNearestNeighbors(points, query_point, k)

        self.assertEqual(len(result), 0)

    def test_find_k_nearest_neighbors_all_points_equidistant(self):
        knn = Answer()
        points = [
            Answer.Point(2, 3),
            Answer.Point(3, 2),
            Answer.Point(1, 2),
            Answer.Point(2, 1)
        ]
        query_point = Answer.Point(2, 2)
        k = 2
        result = knn.findKNearestNeighbors(points, query_point, k)

        self.assertEqual(len(result), 2)
        self.assertTrue(self.contains_point(result, Answer.Point(2, 3)))
        self.assertTrue(self.contains_point(result, Answer.Point(3, 2)))

    def contains_point(self, points, point):
        for p in points:
            if math.isclose(p.x, point.x, abs_tol=0.001) and math.isclose(p.y, point.y, abs_tol=0.001):
                return True
        return False
