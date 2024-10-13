describe('TestDataframeToMarkdown', () => {
    beforeEach(() => {
        // Create a sample DataFrame
        this.data = [{ Name: 'Alice', Age: 25 }, { Name: 'Bob', Age: 30 }];
        this.df = this.data;
    });

    it('should write the correct markdown to a file', () => {
        const expectedMarkdown = "| Name   |   Age |\n|:-------|------:|\n| Alice  |    25 |\n| Bob    |    30 |";
        const result = dataframeToMarkdown(this.data, 'dummy_path.md');
        expect(result).toEqual(expectedMarkdown);
    });

    it('should handle an empty DataFrame correctly', () => {
        const dfEmpty = [];
        const expectedMarkdown = "";
        const result = dataframeToMarkdown(dfEmpty, 'dummy_path.md');
        expect(result).toEqual(expectedMarkdown);
    });

    it('should handle a single-row DataFrame correctly', () => {
        const dfSingleRow = [{ Name: 'Alice', Age: 30 }];
        const expectedMarkdown = "| Name   |   Age |\n|:-------|------:|\n| Alice  |    30 |";
        const result = dataframeToMarkdown(dfSingleRow, 'dummy_path.md');
        expect(result).toEqual(expectedMarkdown);
    });

    it('should handle non-string columns correctly', () => {
        const dfNonString = [{ Name: 'Alice', Age: 25, Height: 5.5 }, { Name: 'Bob', Age: 30, Height: 6.0 }];
        const expectedMarkdown = '| Name   |   Age |   Height |\n|:-------|------:|---------:|\n| Alice  |    25 |      5.5 |\n| Bob    |    30 |      6   |';
        const result = dataframeToMarkdown(dfNonString, 'dummy_path.md');
        expect(result).toEqual(expectedMarkdown);
    });

    it('should handle special characters in DataFrame correctly', () => {
        const dfSpecialChars = [{ Name: 'Alice', Comments: 'Good@Work!' }, { Name: 'Bob', Comments: 'Excellent & Commendable' }];
        const expectedMarkdown = '| Name   | Comments                |\n|:-------|:------------------------|\n| Alice  | Good@Work!              |\n| Bob    | Excellent & Commendable |';
        const result = dataframeToMarkdown(dfSpecialChars, 'dummy_path.md');
        expect(result).toEqual(expectedMarkdown);
    });
});