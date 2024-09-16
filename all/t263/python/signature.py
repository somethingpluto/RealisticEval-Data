from typing import List


class MatrixTraversal:
    def spiral_traversal(self, matrix: List[List[int]]) -> List[int]:
        """
        Traverse a given m x n matrix in a spiral order and return all elements as a list.

        The function starts at the top-left corner of the matrix and traverses it in a
        clockwise spiral order, moving right across the top row, down the right column,
        left across the bottom row, and up the left column, repeating this process
        until all elements are traversed.

        Args:
            matrix (List[List[int]]): A 2D list representing the matrix with m rows and n columns.

        Returns:
            List[int]: A list of integers representing the elements of the matrix
            in the order they were traversed.
        """