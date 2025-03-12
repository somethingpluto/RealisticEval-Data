import { Table } from 'pretty-table';

function calculateColumnWidths(data: string[][]): number[] {
  // ... existing code ...

  // Sort the widths array in descending order
  const sortedWidths = widths.slice().sort((a, b) => b - a);

  // Create a new Pretty Table instance
  const table = new Table();

  // Add columns to the table with the calculated widths
  sortedWidths.forEach((width, index) => {
    table.columns[index] = { width };
  });

  // Add rows to the table
  data.forEach(row => {
    table.push(row);
  });

  // Print the table
  console.log(table.toString());

  // Return the sorted widths
  return sortedWidths;
}
describe('TestCalculateColumnWidths', () => {
    it('should handle a standard case', () => {
      const data = [
        ["Name", "Age", "City"],
        ["Alice", "22", "New York"],
        ["Bob", "30", "San Francisco"]
      ];
      const expected = [5, 3, 13];
      expect(calculateColumnWidths(data)).toEqual(expected);
    });
  
    it('should handle a single element case', () => {
      const data = [["Name"]];
      const expected = [4];
      expect(calculateColumnWidths(data)).toEqual(expected);
    });
  
    it('should handle varied length cases', () => {
      const data = [
        ["a", "bb", "ccc"],
        ["dddd", "ee", "f"]
      ];
      const expected = [4, 2, 3];
      expect(calculateColumnWidths(data)).toEqual(expected);
    });
  
    it('should handle all empty strings', () => {
      const data = [
        ["", "", ""],
        ["", "", ""]
      ];
      const expected = [0, 0, 0];
      expect(calculateColumnWidths(data)).toEqual(expected);
    });
  
    it('should handle mixed content', () => {
      const data = [
        ["1234", "567", "890"],
        ["abc", "defg", "h"]
      ];
      const expected = [4, 4, 3];
      expect(calculateColumnWidths(data)).toEqual(expected);
    });
  
    it('should handle a single column with multiple rows', () => {
      const data = [
        ["one"],
        ["two"],
        ["three"]
      ];
      const expected = [5];
      expect(calculateColumnWidths(data)).toEqual(expected);
    });
  });
