function spiralTraversal(matrix: number[][]): number[] {
  if (matrix.length === 0) {
      return [];
  }

  const m: number = matrix.length;
  const n: number = matrix[0].length;
  let rowStart: number = 0, rowEnd: number = m - 1;
  let colStart: number = 0, colEnd: number = n - 1;
  let result: number[] = [];

  while (rowStart <= rowEnd && colStart <= colEnd) {
      // Traverse Right along the top row
      for (let j = colStart; j <= colEnd; j++) {
          result.push(matrix[rowStart][j]);
      }
      rowStart++;

      // Traverse Down along the right column
      for (let i = rowStart; i <= rowEnd; i++) {
          result.push(matrix[i][colEnd]);
      }
      colEnd--;

      // Traverse Left along the bottom row, if still within bounds
      if (rowStart <= rowEnd) {
          for (let j = colEnd; j >= colStart; j--) {
              result.push(matrix[rowEnd][j]);
          }
          rowEnd--;
      }

      // Traverse Up along the left column, if still within bounds
      if (colStart <= colEnd) {
          for (let i = rowEnd; i >= rowStart; i--) {
              result.push(matrix[i][colStart]);
          }
          colStart++;
      }
  }

  return result;
}