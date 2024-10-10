describe('alignLinesLeft', () => {
  it('should align two lines of string to the left', () => {
      expect(alignLinesLeft("hello", "world")).toEqual(["hello ", "world "]);
      expect(alignLinesLeft("short", "longerstring")).toEqual(["short   ", "longerstring"]);
      expect(alignLinesLeft("", "nonempty")).toEqual(["     ", "nonempty"]);
      expect(alignLinesLeft("equal", "equal")).toEqual(["equal", "equal"]);
  });
});