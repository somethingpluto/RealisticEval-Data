"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

from typing import List

class Solution:
    #code generated with chatgpt
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        row_start, row_end = 0, m - 1
        col_start, col_end = 0, n - 1
        res = []

        while row_start <= row_end and col_start <= col_end:
            # Traverse Right
            for j in range(col_start, col_end + 1):
                res.append(matrix[row_start][j])
            row_start += 1
            
            # Traverse Down
            for i in range(row_start, row_end + 1):
                res.append(matrix[i][col_end])
            col_end -= 1
            
            # Traverse Left
            if row_start <= row_end:
                for j in range(col_end, col_start - 1, -1):
                    res.append(matrix[row_end][j])
                row_end -= 1
            
            # Traverse Up
            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    res.append(matrix[i][col_start])
                col_start += 1

        return res
         



s = Solution()
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[3],[2]]
matrix =[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(s.spiralOrder(matrix))