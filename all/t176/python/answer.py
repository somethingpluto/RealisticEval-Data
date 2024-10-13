import math
import heapq
from typing import List


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        """Calculate the Euclidean distance to another point."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def find_k_nearest_neighbors(points: List[Point], query_point: Point, k: int) -> List[Point]:
    """Find the k nearest neighbors to the query_point."""
    # Max-heap to store the k closest points
    max_heap = []

    for point in points:
        distance = point.distance_to(query_point)
        if len(max_heap) < k:
            heapq.heappush(max_heap, (-distance, point))  # Push negative distance for max-heap behavior
        elif distance < -max_heap[0][0]:  # Compare with the max distance in the heap
            heapq.heappop(max_heap)  # Remove the farthest point
            heapq.heappush(max_heap, (-distance, point))

    # Extract the points from the heap and return them
    return [point for (_, point) in max_heap]
