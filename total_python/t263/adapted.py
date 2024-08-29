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
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        row_start, row_end = 0, m - 1
        col_start, col_end = 0, n - 1
        result = []

        while row_start <= row_end and col_start <= col_end:
            # Traverse Right along the top row
            for j in range(col_start, col_end + 1):
                result.append(matrix[row_start][j])
            row_start += 1

            # Traverse Down along the right column
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1

            # Traverse Left along the bottom row, if still within bounds
            if row_start <= row_end:
                for j in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][j])
                row_end -= 1

            # Traverse Up along the left column, if still within bounds
            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1

        return result


